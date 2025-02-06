# -*- coding: utf-8 -*-
"""
Engine to train the surrogate

"""
from copy import deepcopy
import os
from itertools import cycle
import joblib
import corner
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import distance
import seaborn as sns
from sklearn.metrics import r2_score
from matplotlib.backends.backend_pdf import PdfPages

from bayesvalidrox.bayes_inference.rejection_sampler import RejectionSampler
from .sequential_design import SequentialDesign
from .supplementary import hellinger_distance, root_mean_squared_error
from .polynomial_chaos import PCE
from .meta_model import MetaModel as MM


class Engine:
    """
    Engine

    This class is responsible for collecting and managing the experimental
    design, the model and the metamodel for training and evaluations.

    Attributes
    ----------
    meta_model : obj
        A bvr.MetaModel object. If no MetaModel should be trained and used, set
        this to None.
    model : obj
        A model interface of type bvr.PyLinkForwardModel that can be run.
    exp_design : obj
        The experimental design that will be used to sample from the input
        space.
    discrepancy : obj, optional
        A bvr.Discrepancy object that describes the model uncertainty, i.e. the diagonal entries
        of the variance matrix for a multivariate normal likelihood. This is used
        during active learning. The default is None.

    """

    def __init__(self, meta_model, model, exp_design, discrepancy=None):
        self.meta_model = meta_model
        self.model = model
        self.exp_design = exp_design
        self.discrepancy = discrepancy
        self.parallel = False
        self.trained = False

        # Init other parameters
        self.bound_tuples = None
        self.lc_error = None
        self.observations = None
        self.out_names = None
        self.seq_min_dist = None
        self.seq_des = None
        self.seq_rmse_mean = None
        self.seq_rmse_std = None
        self.seq_kld = None
        self.seq_dist_hellinger = None
        self.seq_bme = None
        self.seq_valid_error = None
        self.seq_modified_loo = None
        self.valid_likelihoods = None
        self._y_hat_prev = None
        self.emulator = False
        self.verbose = False
        self.plot = False

    def start_engine(self) -> None:
        """
        Do all the preparations that need to be run before the actual training

        Returns
        -------
        None

        """
        self.out_names = self.model.output.names
        self.exp_design.out_names = self.out_names
        if isinstance(self.meta_model, MM):
            self.emulator = True
            self.meta_model.out_names = self.out_names
            if self.verbose:
                print("MetaModel has been given, `emulator` will be set to `True`")
        else:
            self.emulator = False
            if self.verbose:
                print("MetaModel has not been given, `emulator` will be set to `False`")

    def train_normal(self, parallel=False, verbose=False, save=False) -> None:
        """
        Trains surrogate on static samples only.
        Samples are taken from the experimental design and the specified
        model is run on them.
        Alternatively the samples can be read in from a provided hdf5 file.
        save: bool determines whether the trained surrogate and the hdf5 file should be saved


        Returns
        -------
        None

        """
        self.verbose = verbose
        self.start_engine()

        exp_design = self.exp_design
        meta_model = self.meta_model

        # Prepare X samples
        max_deg = np.max(meta_model.pce_deg) if self.emulator else 1
        exp_design.generate_ed(max_deg=max_deg)

        # Run simulations at X
        if not hasattr(exp_design, "y") or exp_design.y is None:
            print("\n Now the forward model needs to be run!\n")

            self.model.delete_hdf5()

            y_train, new_x_train = self.model.run_model_parallel(
                exp_design.x, mp=parallel, store_hdf5=save
            )
            exp_design.x = new_x_train
            exp_design.y = y_train
        else:
            # Check if a dict has been passed.
            if not isinstance(exp_design.y, dict):
                raise TypeError(
                    "Please provide either a dictionary or a hdf5"
                    "file to exp_design.hdf5_file argument."
                )

        # Separate output dict and x-values
        if "x_values" in exp_design.y:
            exp_design.x_values = exp_design.y["x_values"]
            del exp_design.y["x_values"]
        else:
            if self.verbose:
                print(
                    "No x_values are given, this might lead to issues during PostProcessing"
                )

        # Fit the surrogate
        if self.emulator:
            meta_model.fit(
                exp_design.x, exp_design.y, parallel=parallel, verbose=verbose
            )

        # Save what there is to save
        if save:
            # Save surrogate
            if not os.path.exists("surrogates/"):
                os.makedirs("surrogates/")
            with open(f"surrogates/surrogate_{self.model.name}.pk1", "wb") as output:
                joblib.dump(meta_model, output, 2)

            # Zip the model run directories
            if (
                self.model.link_type.lower() == "pylink"
                and self.exp_design.sampling_method.lower() != "user"
            ):
                self.model.zip_subdirs(self.model.name, f"{self.model.name}_")

        # Set that training was done
        self.trained = True

    # -------------------------------------------------------------------------
    def eval_metamodel(
        self,
        samples=None,
        nsamples=None,
        sampling_method="random",
        return_samples=False,
        parallel=False,
    ):
        """
        Evaluates metamodel at the requested samples. One can also generate
        nsamples.

        Parameters
        ----------
        samples : array of shape (n_samples, n_params), optional
            Samples to evaluate metamodel at. The default is None.
        nsamples : int, optional
            Number of samples to generate, if no `samples` is provided. The
            default is None.
        sampling_method : str, optional
            Type of sampling, if no `samples` is provided. The default is
            'random'.
        return_samples : bool, optional
            Retun samples, if no `samples` is provided. The default is False.
        parallel : bool, optional
            Set to True if the evaluations should be done in parallel.
            The default is False.

        Returns
        -------
        mean_pred : dict
            Mean of the predictions.
        std_pred : dict
            Standard deviatioon of the predictions.
        """
        # Generate samples
        if samples is None:
            samples = self.exp_design.generate_samples(nsamples, sampling_method)

        # Evaluate Model or MetaModel
        if self.emulator:
            # MetaModel does internal transformation to other space
            mean_pred, std_pred = self.meta_model.eval_metamodel(samples)
        else:
            mean_pred, _ = self.model.run_model_parallel(samples, mp=parallel)

        if return_samples:
            if self.emulator:
                return mean_pred, std_pred, samples
            return mean_pred, samples
        if self.emulator:
            return mean_pred, std_pred
        return mean_pred, None

    # -------------------------------------------------------------------------

    def train_sequential(self, parallel=False, verbose=False, plot=False) -> None:
        """
        Train the surrogate in a sequential manner.
        First build and train evereything on the static samples, then iterate
        choosing more samples and refitting the surrogate on them.

        Parameters
        ----------
        parallel : bool, optional
            Toggles parallelization in the MetaModel training.
            The default is False
        verbose : bool, optional
            Toggles verbose outputs during training.
            The default is False.
        plot : bool, optional
            Toggles the generation of plots for each sequential iteration.
            The default is False.

        Returns
        -------
        None

        """

        # Initialization
        self.seq_modified_loo = {}
        self.seq_valid_error = {}
        self.seq_bme = {}
        self.seq_kld = {}
        self.seq_dist_hellinger = {}
        self.seq_rmse_mean = {}
        self.seq_rmse_std = {}
        self.seq_min_dist = []

        self.parallel = parallel
        self.plot = plot
        self.start_engine()

        if (
            not hasattr(self.meta_model, "valid_samples")
            or self.meta_model.valid_samples is None
        ):
            self.exp_design.valid_samples = []
            self.exp_design.valid_model_runs = []
            self.valid_likelihoods = []

        # Determine the meta_model type
        pce = bool(
            self.meta_model.meta_model_type.lower() != "gpe"
            and isinstance(self.meta_model, PCE)
        )

        # mc_ref = True if bool(self.model.mc_reference) else False
        mc_ref = False
        # Get issues from these comparisons, thus doubled it here
        if self.model.mc_reference is not {}:
            mc_ref = True
            self.model.read_observation("mc_ref")
        if self.model.mc_reference is not None:
            mc_ref = True
            self.model.read_observation("mc_ref")

        # Get the parameters
        max_n_samples = self.exp_design.n_max_samples
        mod_loo_threshold = self.exp_design.mod_loo_threshold
        n_canddidate = self.exp_design.n_canddidate
        n_replication = self.exp_design.n_replication
        util_func = self.exp_design.util_func
        output_name = self.out_names

        # Setup the Sequential Design object
        self.seq_des = SequentialDesign(
            self.meta_model,
            self.model,
            self.exp_design,
            self,
            self.discrepancy,
            out_names=self.out_names,
        )

        # Handle if only one UtilityFunctions is provided
        if not isinstance(util_func, list):
            util_func = [self.exp_design.util_func]

        # Read observations or MC-reference
        if (
            len(self.model.observations) != 0 or self.model.meas_file is not None
        ) and hasattr(self, "discrepancy"):
            self.observations = self.model.read_observation()
            self.discrepancy.build_discrepancy()
        else:
            self.observations = []

        # ---------- Initial self.meta_model ----------
        if not self.trained:
            self.train_normal(parallel=parallel, verbose=verbose)
        init_meta_model = deepcopy(self.meta_model)

        # Validation error if validation set is provided.
        if self.exp_design.valid_model_runs:
            init_rmse, init_valid_error = self._valid_error()  # init_mmeta_model)
            init_valid_error = list(init_valid_error.values())
        else:
            init_rmse = None

        # Check if discrepancy is provided
        if len(self.observations) != 0 and hasattr(self, "discrepancy"):
            # Calculate the initial BME
            out = self._bme_calculator(self.observations, init_rmse)
            init_bme, init_kld, init_post, _, init_dist_hellinger = out
            print(f"\nInitial BME: {init_bme:.2f}")
            print(f"Initial KLD: {init_kld:.2f}")

            # Posterior snapshot (initial)
            if plot:
                par_names = self.exp_design.par_names
                print("Posterior snapshot (initial) is being plotted...")
                self.plot_posterior(init_post, par_names, "SeqPosterior_init")

        # Check the convergence of the Mean & Std
        if mc_ref and pce:
            init_rmse_mean, init_rmse_std = self._error_mean_std()
            print(
                f"Initial Mean and Std error: {init_rmse_mean:.2f},"
                f" {init_rmse_std:.2f}"
            )

        # Read the initial experimental design
        x_init = self.exp_design.x
        init_n_samples = len(self.exp_design.x)
        init_y_prev = self.exp_design.y
        init_lc_error = init_meta_model.lc_error
        n_itrs = max_n_samples - init_n_samples

        # Get some initial statistics
        # Read the initial modified_loo
        init_mod_loo = []
        if pce:
            scores_all, var_expdes_y = [], []
            for out_name in output_name:
                y = self.exp_design.y[out_name]
                scores_all.append(
                    list(self.meta_model.loocv_score_dict["b_1"][out_name].values())
                )
                if self.meta_model.dim_red_method.lower() == "pca":
                    pca = self.meta_model.pca["b_1"][out_name]
                    components = pca.transform(y)
                    var_expdes_y.append(np.var(components, axis=0))
                else:
                    var_expdes_y.append(np.var(y, axis=0))

            scores = [item for sublist in scores_all for item in sublist]
            weights = [item for sublist in var_expdes_y for item in sublist]
            init_mod_loo = [
                np.average([1 - score for score in scores], weights=weights)
            ]

        prev_meta_model_dict = {}
        # Can run sequential design multiple times for comparison
        for rep_idx in range(n_replication):
            print(f"\n>>>> Replication: {rep_idx + 1}<<<<")

            # util_func: the function to use inside the type of exploitation
            for util_f in util_func:
                print(f"\n>>>> Utility Function: {util_f} <<<<")
                # To avoid changes ub original aPCE object
                self.exp_design.x = x_init
                self.exp_design.y = init_y_prev
                self.exp_design.lc_error = init_lc_error

                # Set the experimental design
                x_prev = x_init
                total_n_samples = init_n_samples
                y_prev = init_y_prev
                x_full = []

                # Store the initial modified_loo
                if pce:
                    print("\nInitial modified_loo:", init_mod_loo)
                    seq_modified_loo = np.array(init_mod_loo)

                if len(self.exp_design.valid_model_runs) != 0:
                    seq_valid_error = np.array(init_valid_error)

                # Check if data is provided
                if len(self.observations) != 0 and hasattr(self, "discrepancy"):
                    seq_bme = np.array([init_bme])
                    seq_kld = np.array([init_kld])
                    seq_dist_hellinger = np.array([init_dist_hellinger])

                if mc_ref and pce:
                    seq_rmse_mean = np.array([init_rmse_mean])
                    seq_rmse_std = np.array([init_rmse_std])

                # ------- Start Sequential Experimental Design -------
                postcnt = 1
                for itr_no in range(1, n_itrs + 1):
                    print(f"\n>>>> Iteration number {itr_no} <<<<")

                    # Save the meta_model prediction before updating
                    prev_meta_model_dict[itr_no] = deepcopy(self.meta_model)
                    if itr_no > 1:
                        pc_model = prev_meta_model_dict[itr_no - 1]
                        self.seq_des._y_hat_prev, _ = pc_model.eval_metamodel(
                            x_full[-1].reshape(1, -1)
                        )
                        del prev_meta_model_dict[itr_no - 1]
                    if itr_no == 1 and self.exp_design.tradeoff_scheme == "adaptive":
                        pc_model = prev_meta_model_dict[itr_no]
                        self.seq_des._y_hat_prev, _ = pc_model.eval_metamodel(x_prev)

                    # Optimal Bayesian Design
                    x_new, updated_prior = self.seq_des.choose_next_sample(
                        n_canddidate, util_f
                    )
                    s = np.min(distance.cdist(x_init, x_new, "euclidean"))
                    self.seq_min_dist.append(s)
                    print(f"\nmin Dist from OldExpDesign: {s:2f}")
                    print("\n")

                    # Evaluate the full model response at the new sample
                    y_new, _ = self.model.run_model_parallel(
                        x_new, prev_run_no=total_n_samples
                    )
                    total_n_samples += x_new.shape[0]

                    # ------ Plot the surrogate model vs Origninal Model ------
                    if self.plot:
                        y_hat, std_hat = self.meta_model.eval_metamodel(x_new)
                        self.plot_adapt(
                            self.meta_model, y_new, y_hat, std_hat, plot_ed=False
                        )

                    # -------- Retrain the surrogate model -------
                    # Extend new experimental design
                    x_full = np.vstack((x_prev, x_new))

                    # Updating experimental design Y
                    for out_name in output_name:
                        y_full = np.vstack((y_prev[out_name], y_new[out_name]))
                        self.exp_design.y[out_name] = y_full

                    # Pass new design to the meta_model object
                    self.exp_design.sampling_method = "user"
                    self.exp_design.x = x_full

                    # Save the Experimental Design for next iteration
                    x_prev = x_full
                    y_prev = self.exp_design.y

                    # Pass the new prior as the input
                    self.meta_model.input_obj.poly_coeffs_flag = False
                    if updated_prior is not None:
                        self.meta_model.input_obj.poly_coeffs_flag = True
                        print("updated_prior:", updated_prior.shape)
                        for i in range(updated_prior.shape[1]):
                            self.meta_model.input_obj.marginals[i].dist_type = None
                            x = updated_prior[:, i]
                            self.meta_model.input_obj.marginals[i].raw_data = x

                    # Train the surrogate model for new exp_design
                    self.train_normal(parallel=False)

                    # -------- Evaluate the retrained surrogate model -------
                    # Extract Modified LOO from Output
                    if pce:
                        scores_all, var_expdes_y = [], []
                        for out_name in output_name:
                            y = self.exp_design.y[out_name]
                            scores_all.append(
                                list(
                                    self.meta_model.loocv_score_dict["b_1"][
                                        out_name
                                    ].values()
                                )
                            )
                            if self.meta_model.dim_red_method.lower() == "pca":
                                pca = self.meta_model.pca["b_1"][out_name]
                                components = pca.transform(y)
                                var_expdes_y.append(np.var(components, axis=0))
                            else:
                                var_expdes_y.append(np.var(y, axis=0))
                        scores = [item for sublist in scores_all for item in sublist]
                        weights = [item for sublist in var_expdes_y for item in sublist]
                        modified_loo = [
                            np.average([1 - score for score in scores], weights=weights)
                        ]

                        print("\n")
                        print(f"Updated modified_loo {util_f}:\n", modified_loo)
                        print("\n")

                    # Compute the validation error
                    if self.exp_design.valid_model_runs:
                        rmse, valid_error = self._valid_error()  # self.meta_model)
                        valid_error = list(valid_error.values())
                    else:
                        rmse = None

                    # Store updated modified_loo
                    if pce:
                        seq_modified_loo = np.vstack((seq_modified_loo, modified_loo))
                        if len(self.exp_design.valid_model_runs) != 0:
                            seq_valid_error = np.vstack((seq_valid_error, valid_error))
                    # -------- Caclulation of bme as accuracy metric -------
                    # Check if data is provided
                    if len(self.observations) != 0:
                        # Calculate the initial bme
                        out = self._bme_calculator(self.observations, rmse)
                        bme, kld, posterior, _, dist_hellinger = out
                        print("\n")
                        print(f"Updated BME: {bme:.2f}")
                        print(f"Updated KLD: {kld:.2f}")
                        print("\n")

                        # Plot some snapshots of the posterior
                        if self.plot:
                            par_names = self.exp_design.par_names
                            print("Posterior snapshot is being plotted...")
                            self.plot_posterior(
                                posterior, par_names, f"SeqPosterior_{postcnt}"
                            )
                        postcnt += 1

                    # Check the convergence of the Mean&Std
                    if mc_ref and pce:
                        print("\n")
                        rmse_mean, rmse_std = self._error_mean_std()
                        print(
                            f"Updated Mean and Std error: {rmse_mean:.2f}, "
                            f"{rmse_std:.2f}"
                        )
                        print("\n")

                    # Store the updated bme & kld
                    # Check if data is provided
                    if len(self.observations) != 0:
                        seq_bme = np.vstack((seq_bme, bme))
                        seq_kld = np.vstack((seq_kld, kld))
                        seq_dist_hellinger = np.vstack(
                            (seq_dist_hellinger, dist_hellinger)
                        )
                    if mc_ref and pce:
                        seq_rmse_mean = np.vstack((seq_rmse_mean, rmse_mean))
                        seq_rmse_std = np.vstack((seq_rmse_std, rmse_std))

                    if pce and any(LOO < mod_loo_threshold for LOO in modified_loo):
                        break

                    # Clean up
                    if len(self.observations) != 0:
                        del out
                    print()
                    print("-" * 50)
                    print()

                # Store updated modified_loo and bme in dictonary
                str_key = f"{util_f}_rep_{rep_idx + 1}"
                if pce:
                    self.seq_modified_loo[str_key] = seq_modified_loo
                if len(self.exp_design.valid_model_runs) != 0:
                    self.seq_valid_error[str_key] = seq_valid_error

                # Check if data is provided
                if len(self.observations) != 0:
                    self.seq_bme[str_key] = seq_bme
                    self.seq_kld[str_key] = seq_kld
                if (
                    hasattr(self.meta_model, "valid_likelihoods")
                    and self.valid_likelihoods
                ):
                    self.seq_dist_hellinger[str_key] = seq_dist_hellinger
                if mc_ref and pce:
                    self.seq_rmse_mean[str_key] = seq_rmse_mean
                    self.seq_rmse_std[str_key] = seq_rmse_std

    # -------------------------------------------------------------------------
    def plot_posterior(self, posterior, par_names, key):
        """
        Plot the posterior of a specific key as a corner plot

        Parameters
        ----------
        posterior : 2d np.array
            Samples of the posterior.
        par_names : list of strings
            List of the parameter names.
        key : string
            Output key that this posterior belongs to.

        """

        # Initialization
        newpath = r"Outputs_SeqPosteriorComparison/posterior"
        os.makedirs(newpath, exist_ok=True)

        bound_tuples = self.exp_design.bound_tuples
        n_params = len(par_names)
        font_size = 40
        if n_params == 2:

            fig_posterior, ax = plt.subplots(figsize=(15, 15))

            sns.kdeplot(
                x=posterior[:, 0],
                y=posterior[:, 1],
                fill=True,
                ax=ax,
                cmap=plt.cm.jet,
                clip=bound_tuples,
            )
            # Axis labels
            plt.xlabel(par_names[0], fontsize=font_size)
            plt.ylabel(par_names[1], fontsize=font_size)

            # Set axis limit
            plt.xlim(bound_tuples[0])
            plt.ylim(bound_tuples[1])

            # Increase font size
            plt.xticks(fontsize=font_size)
            plt.yticks(fontsize=font_size)

            # Switch off the grids
            plt.grid(False)

        else:
            fig_posterior = corner.corner(
                posterior,
                labels=par_names,
                title_fmt=".2e",
                show_titles=True,
                title_kwargs={"fontsize": 12},
            )

        fig_posterior.savefig(f"./{newpath}/{key}.pdf", bbox_inches="tight")
        plt.close()

        # Save the posterior as .npy
        np.save(f"./{newpath}/{key}.npy", posterior)

    # -------------------------------------------------------------------------
    def _bme_calculator(self, obs_data, rmse=None):
        """
        This function computes the Bayesian model evidence (BME) via Monte
        Carlo integration.

        Parameters
        ----------
        obs_data : dict of 1d np arrays
            Observed data.
        rmse : dict of floats, optional
            RMSE values for each output-key. The dafault is None.

        Returns
        -------
        (log_bme, kld, x_post, likelihoods, dist_hellinger)

        """
        # Initializations
        sampling_method = "random"
        mc_size = 10000
        ess = 0
        # Estimation of the integral via Monte Varlo integration
        while (ess > mc_size) or (ess < 1):

            # Generate samples for Monte Carlo simulation
            x_mc = self.exp_design.generate_samples(mc_size, sampling_method)

            # Monte Carlo simulation for the candidate design
            y_mc, std_mc = self.meta_model.eval_metamodel(x_mc)

            # Rejection step
            sampler = RejectionSampler(
                prior_samples=x_mc,
                use_emulator=False,
                out_names=self.out_names,
                observation=obs_data,
                discrepancy=self.discrepancy,
            )
            sampler.posterior = sampler.run_sampler(
                outputs=y_mc,
                surr_error=rmse,
                std_outputs=std_mc,
                consider_samplesize=True,
                recalculate_loglik=True,
            )

            # Enlarge sample size if it doesn't fulfill the criteria
            ess = sampler.ess
            if (ess > mc_size) or (ess < 1):
                mc_size *= 10
                print(f"ess={ess}, increasing the MC size to {mc_size}.")

        # Validation metrics
        kld, _ = sampler.calculate_valid_metrics(self.exp_design)
        likelihoods = sampler.likelihoods

        # Plot likelihood vs refrence
        dist_hellinger = 0.0
        if self.plot and self.valid_likelihoods is not None:
            # Init output directory
            newpath = r"Outputs_SeqPosteriorComparison/likelihood_vs_ref"
            os.makedirs(newpath, exist_ok=True)

            # Hellinger distance
            valid_likelihoods = np.array(self.valid_likelihoods)
            ref_like = np.log(valid_likelihoods[(valid_likelihoods > 0)])
            est_like = np.log(likelihoods[likelihoods > 0])
            dist_hellinger = hellinger_distance(ref_like, est_like)

            idx = len(
                [
                    name
                    for name in os.listdir(newpath)
                    if "likelihoods_" in name
                    and os.path.isfile(os.path.join(newpath, name))
                ]
            )

            fig, ax = plt.subplots()
            try:
                sns.kdeplot(
                    np.log(valid_likelihoods[valid_likelihoods > 0]),
                    shade=True,
                    color="g",
                    label="Ref. Likelihood",
                )
                sns.kdeplot(
                    np.log(likelihoods[likelihoods > 0]),
                    shade=True,
                    color="b",
                    label="Likelihood with PCE",
                )
            except:
                pass

            text = (
                f"Hellinger Dist.={dist_hellinger:.3f}\n logBME={sampler.log_bme:.3f}"
                "\n DKL={kld:.3f}"
            )

            plt.text(
                0.05,
                0.75,
                text,
                bbox={
                    "facecolor": "wheat",
                    "edgecolor": "black",
                    "boxstyle": "round,pad=1",
                },
                transform=ax.transAxes,
            )

            fig.savefig(f"./{newpath}/likelihoods_{idx}.pdf", bbox_inches="tight")
            plt.close()

        return (
            sampler.log_bme,
            kld,
            sampler.posterior,
            sampler.likelihoods,
            dist_hellinger,
        )

    # -------------------------------------------------------------------------
    def _valid_error(self):
        """
        Evaluate the meta_model on the validation samples and calculate the
        error against the corresponding model runs

        Returns
        -------
        rms_error : dict
            RMSE for each validation run.
        valid_error : dict
            Normed (?)RMSE for each validation run.

        """
        # Obtain model and surrogate outputs
        valid_model_runs = self.exp_design.valid_model_runs
        valid_metamod_runs, _ = self.meta_model.eval_metamodel(
            self.exp_design.valid_samples
        )

        # Loop over the keys and compute RMSE error.
        rms_error = {}
        valid_error = {}
        for key in self.out_names:
            rms_error[key] = root_mean_squared_error(
                valid_model_runs[key], valid_metamod_runs[key]
            )

            # Validation error
            valid_error[key] = np.power(rms_error[key], 2)
            valid_error[key] /= np.var(valid_model_runs[key], ddof=1, axis=0)

            # Report table
            print(f"\n>>>>> Updated Errors of {key} <<<<<")
            print("\nIndex  |  RMSE   |  Validation Error")
            print("-" * 35)
            print(
                "\n".join(
                    f"{i + 1}  |  {k:.3e}  |  {j:.3e}"
                    for i, (k, j) in enumerate(zip(rms_error[key], valid_error[key]))
                )
            )

        return rms_error, valid_error

    # -------------------------------------------------------------------------
    def _error_mean_std(self):
        """
        Calculates the error in the overall mean and std approximation of the
        surrogate against the mc-reference provided to the model.

        Returns
        -------
        rmse_mean : float
            RMSE of the means
        rmse_std : float
            RMSE of the standard deviations

        """
        if self.model.mc_reference is {}:
            raise AttributeError(
                "Model.mc_reference needs to be given to calculate the surrogate error!"
            )

        # Compute the mean and std based on the meta_model
        means, stds = self.meta_model.calculate_moments()

        rmse_mean, rmse_std = 0, 0
        # Compute the root mean squared error between metamodel outputs and mc ref
        for output in self.out_names:
            if self.model.mc_reference is None:
                raise AttributeError(
                    "Model.mc_reference needs to be given to calculate the error mean!"
                )

            print(f"Reference mean: {self.model.mc_reference}")

            rmse_mean += root_mean_squared_error(
                self.model.mc_reference["mean"], means[output]
            )
            rmse_std += root_mean_squared_error(
                self.model.mc_reference["std"], stds[output]
            )

        return rmse_mean, rmse_std

    def plot_adapt(
        self, y_mod, y_metamod, y_metamod_std, x_values=None, plot_ed=False, save=True
    ):
        """
        Visualize the model and metamodel outputs

        Parameters
        ----------
        y_mod : dict
            Model outputs.
        y_metamod : dict
            Mean MetaModel outputs.
        y_metamod_std : dict
            Std of MetaModel outputs.
        x_values : list, optional
            Values to write on the x-axis.
            The default is None
        plot_ed : bool, optional
            Toggles plotting the training samples as well.
            The default is False.
        save : bool, optional
            Toggles saving the figure.
            The defautl is True.

        """
        n_samples = self.exp_design.n_new_samples
        itr_nr = (
            1
            + (self.exp_design.x.shape[0] - self.exp_design.n_init_samples) // n_samples
        )
        old_ed_y = self.exp_design.y
        if x_values is None:
            x_values = []

        if save:
            newpath = "adaptivePlots"
            os.makedirs(newpath, exist_ok=True)
            pdf = PdfPages(f"./{newpath}/Model_vs_engine_itr_{itr_nr}.pdf")

        # List of markers and colors
        color = cycle((["b", "g", "r", "y", "k"]))
        marker = cycle(("x", "d", "+", "o", "*"))

        x_axis = "Time [s]"

        if len(self.out_names) == 1:
            self.out_names.insert(0, x_axis)
        try:
            x_values = y_mod["x_values"]
        except KeyError:
            x_values = x_values

        fig = plt.figure(figsize=(24, 16))

        # Plot the model vs PCE model
        for _, key in enumerate(self.out_names):
            y_metamod_ = y_metamod[key]
            y_metamod_std_ = y_metamod_std[key]
            y_mod_ = y_mod[key]
            if y_mod_.ndim == 1:
                y_mod_ = y_mod_.reshape(1, -1)
            if isinstance(x_values, dict):
                x = x_values[key]
            else:
                x = x_values

            for idx, y in enumerate(y_mod_):
                col = next(color)
                mark = next(marker)

                plt.plot(
                    x,
                    y,
                    color=col,
                    marker=mark,
                    lw=2.0,
                    label="$Y_{%s}^{M}$" % (idx + itr_nr),
                )

                plt.plot(
                    x,
                    y_metamod_[idx],
                    color=col,
                    marker=mark,
                    lw=2.0,
                    linestyle="--",
                    label="$Y_{%s}^{PCE}$" % (idx + itr_nr),
                )
                plt.fill_between(
                    x,
                    y_metamod_[idx] - 1.96 * y_metamod_std_[idx],
                    y_metamod_[idx] + 1.96 * y_metamod_std_[idx],
                    color=col,
                    alpha=0.15,
                )

                if plot_ed:
                    for output in old_ed_y[key]:
                        plt.plot(x, output, color="grey", alpha=0.1)

            # Calculate the rmse
            rmse = root_mean_squared_error(y_metamod_, y_mod_)
            r_2 = r2_score(y_metamod_.reshape(-1, 1), y_mod_.reshape(-1, 1))

            plt.ylabel(key)
            plt.xlabel(x_axis)
            plt.title(key)

            ax = fig.axes[0]
            ax.legend(loc="best", frameon=True)
            fig.canvas.draw()
            ax.text(
                0.65,
                0.85,
                f"rmse = {round(rmse, 3)}\n$R^2$ = {round(r_2, 3)}",
                transform=ax.transAxes,
                color="black",
                bbox={
                    "facecolor": "none",
                    "edgecolor": "black",
                    "boxstyle": "round,pad=1",
                },
            )
            plt.grid()

            if save:
                pdf.save(fig, bbox_inches="tight")
                plt.clf()
        pdf.close()
