# -*- coding: utf-8 -*-
"""
Engine to train the surrogate
"""
import sys
import time
from copy import deepcopy, copy
import multiprocessing
from joblib import Parallel, delayed
import numpy as np
import scipy.optimize as opt
from scipy import stats, signal, linalg, sparse
from scipy.spatial import distance
from sklearn.metrics import mean_squared_error
from tqdm import tqdm

from bayesvalidrox.bayes_inference.rejection_sampler import RejectionSampler
from .exploration import Exploration
from .supplementary import create_psi, subdomain


class SequentialDesign:
    """
    Contains options for choosing the next training sample iteratively.

    Parameters
    ----------
    meta_model : obj
        A bvr.MetaModel object. If no MetaModel should be trained and used, set
        this to None.
    model : obj
        A model interface of type bvr.PyLinkForwardModel that can be run.
    exp_design : obj
        The experimental design that will be used to sample from the input
        space.
    engine : obj
        A (trained) bvr.Engine object.
    discrepancy : obj
        A bvr.Discrepancy object that describes the model uncertainty, i.e. the diagonal entries
        of the variance matrix for a multivariate normal likelihood.
    parallel : bool, optional
        Set to True if the evaluations should be done in parallel.
        The default is False.
    out_names : list, optional
        The list of requested output keys to be used for the analysis.
        The default is `None`.

    """

    def __init__(
        self,
        meta_model,
        model,
        exp_design,
        engine,
        discrepancy,
        parallel=False,
        out_names=None,
    ):
        self.meta_model = meta_model
        self.model = model
        self.exp_design = exp_design
        self.parallel = parallel
        self.engine = engine
        self.discrepancy = discrepancy

        # Init other parameters
        self._y_hat_prev = None
        self.out_names = out_names if out_names is not None else []
        self.lc_error = None
        self.error_model = None
        self.bound_tuples = []
        self.n_obs = None
        self.observations = None
        self.valid_likelihoods = None
        self.mc_samples = None
        self.results = None
        self.likelihoods = None

        # Build RejectionSampler for Bayesian variations
        self.rej_sampler = RejectionSampler(
            out_names=self.out_names,
            use_emulator=False,
            observation=self.model.observations,
            discrepancy=self.discrepancy,
        )

    # -------------------------------------------------------------------------

    def choose_next_sample(self, n_candidates=5, var="DKL"):
        """
        Runs optimal sequential design.

        Parameters
        ----------
        n_candidates : int, optional
            Number of candidate samples. The default is 5.
        var : string, optional
            Utility function. The default is 'DKL'.

        Raises
        ------
        NameError
            Wrong utility function.

        Returns
        -------
        Xnew : array (n_samples, n_params)
            Selected new training point(s).
        """

        # Initialization
        bounds = self.exp_design.bound_tuples
        n_new_samples = self.exp_design.n_new_samples
        explore_method = self.exp_design.explore_method
        exploit_method = self.exp_design.exploit_method
        n_cand_groups = self.exp_design.n_cand_groups
        tradeoff_scheme = self.exp_design.tradeoff_scheme

        old_ed_x = self.exp_design.x
        old_ed_y = self.exp_design.y.copy()
        ndim = self.exp_design.x.shape[1]

        # -----------------------------------------
        # ----------- CUSTOMIZED METHODS ----------
        # -----------------------------------------
        # Utility function exploit_method provided by user
        if exploit_method.lower() == "user":
            if (
                not hasattr(self.exp_design, "ExploitFunction")
                or self.exp_design.ExploitFunction is None
            ):
                raise AttributeError(
                    "Function `ExploitFunction` not given to the ExpDesign, \
                        thus cannor run user-defined sequential scheme."
                )
            x_new, filtered_samples = self.exp_design.ExploitFunction(self)

            print("\n")
            print("\nXnew:\n", x_new)

            return x_new, filtered_samples

        # Dual-Annealing works differently from the rest, so deal with this first
        # Here exploration and exploitation are performed simulataneously
        if explore_method.lower() == "dual annealing":
            # ------- EXPLORATION: OPTIMIZATION -------
            start_time = time.time()

            # Divide the domain to subdomains
            subdomains = subdomain(bounds, n_new_samples)

            # Multiprocessing
            if self.parallel:
                args = []
                for i in range(n_new_samples):
                    args.append((exploit_method, subdomains[i], var, i))
                with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:

                    # With Pool.starmap_async()
                    results = pool.starmap_async(self.dual_annealing, args).get()

                # Close the pool
                # pool.close()
            # Without multiprocessing
            else:
                results = []
                for i in range(n_new_samples):
                    results.append(
                        self.dual_annealing(exploit_method, subdomains[i], var, i)
                    )

            # New sample
            x_new = np.array([results[i][1] for i in range(n_new_samples)])
            print("\nXnew:\n", x_new)

            # Computational cost
            elapsed_time = time.time() - start_time
            print("\n")
            print(f"Elapsed_time: {round(elapsed_time, 2)} sec.")
            print("-" * 20)

            return x_new, None

        # ------- Calculate Exploration weight -------
        # Compute exploration weight based on trade off scheme
        explore_w, exploit_w = self.tradeoff_weights(
            tradeoff_scheme, old_ed_x, old_ed_y
        )
        print(
            f"\n Exploration weight={explore_w:0.3f} "
            f"Exploitation weight={exploit_w:0.3f}\n"
        )

        # Generate the candidate samples
        # sampling_method = self.exp_design.sampling_method

        # Note: changed this from 'random' for LOOCV
        # if explore_method == 'LOOCV':
        # allCandidates = self.exp_design.generate_samples(n_candidates,
        #                                                     sampling_method)
        # else:
        #     allCandidates, scoreExploration = explore.get_exploration_samples()

        # -----------------------------------------
        # ---------- EXPLORATION METHODS ----------
        # -----------------------------------------
        if explore_method.lower() == "voronoi":
            raise AttributeError("Exploration with voronoi currently not supported!")
        if explore_method.lower() == "loocv":
            # -----------------------------------------------------------------
            # 'LOOCV':
            # Initilize the ExploitScore array

            # Generate random samples
            all_candidates = self.exp_design.generate_samples(n_candidates, "random")

            # Construct error model based on lc_error
            error_model = self.meta_model.create_ModelError(old_ed_x, self.lc_error)
            self.error_model.append(copy(error_model))

            # Evaluate the error models for allCandidates
            e_lc_all_cands, _ = error_model.eval_errormodel(all_candidates)
            # Select the maximum as the representative error
            e_lc_all_cands = np.dstack(e_lc_all_cands.values())
            e_lc_all_cands = np.max(e_lc_all_cands, axis=1)[:, 0]

            # Normalize the error w.r.t the maximum error
            score_exploration = e_lc_all_cands / np.sum(e_lc_all_cands)

        else:
            # ------- EXPLORATION: SPACE-FILLING DESIGN -------
            # Generate candidate samples from Exploration class
            explore = Exploration(self.exp_design, n_candidates)
            explore.w = 100  # * ndim #500
            # Select criterion (mc-intersite-proj-th, mc-intersite-proj)
            explore.mc_criterion = "mc-intersite-proj"
            all_candidates, score_exploration = explore.get_exploration_samples()

        # =============================================================================
        #             # Temp: ---- Plot all candidates -----
        #             if ndim == 2:
        #                 def plotter(points, allCandidates, Method,
        #                             scoreExploration=None):
        #                     """
        #                     unknown
        #
        #                     Parameters
        #                     ----------
        #                     points
        #                     allCandidates
        #                     Method
        #                     scoreExploration
        #
        #                     Returns
        #                     -------
        #
        #                     """
        #                     if Method.lower() == 'voronoi':
        #                         vor = Voronoi(points)
        #                         fig = voronoi_plot_2d(vor)
        #                         ax1 = fig.axes[0]
        #                     else:
        #                         fig = plt.figure()
        #                         ax1 = fig.add_subplot(111)
        #                     ax1.scatter(points[:, 0], points[:, 1], s=10, c='r',
        #                                 marker="s", label='Old Design Points')
        #                     ax1.scatter(allCandidates[:, 0], allCandidates[:, 1], s=10,
        #                                 c='b', marker="o", label='Design candidates')
        #                     for i in range(points.shape[0]):
        #                         txt = 'p' + str(i + 1)
        #                         ax1.annotate(txt, (points[i, 0], points[i, 1]))
        #                     if scoreExploration is not None:
        #                         for i in range(allCandidates.shape[0]):
        #                             txt = str(round(scoreExploration[i], 5))
        #                             ax1.annotate(txt, (allCandidates[i, 0],
        #                                                allCandidates[i, 1]))
        #
        #                     plt.xlim(self.bound_tuples[0])
        #                     plt.ylim(self.bound_tuples[1])
        #                     # plt.show()
        #                     plt.legend(loc='upper left')
        #
        # =============================================================================
        # -----------------------------------------
        # --------- EXPLOITATION METHODS ----------
        # -----------------------------------------
        if (
            exploit_method.lower() == "bayesoptdesign"
            or exploit_method.lower() == "bayesactdesign"
        ):

            # ------- EXPLOITATION: BayesOptDesign & ActiveLearning -------
            if explore_w != 1.0:
                # Check if all needed properties are set
                if not hasattr(self.exp_design, "max_func_itr"):
                    raise AttributeError(
                        "max_func_itr not given to the experimental design"
                    )

                # Create a sample pool for rejection sampling
                mc_size = 15000
                x_mc = self.exp_design.generate_samples(mc_size, "random")

                # Split the candidates in groups for multiprocessing
                split_cand = np.array_split(all_candidates, n_cand_groups, axis=0)
                if self.parallel:
                    results = Parallel(n_jobs=-1, backend="multiprocessing")(
                        delayed(self.run_util_func)(
                            exploit_method, split_cand[i], i, var, x_mc
                        )
                        for i in range(n_cand_groups)
                    )
                else:
                    results = []
                    for i in range(n_cand_groups):
                        results.append(
                            self.run_util_func(
                                exploit_method, split_cand[i], i, var, x_mc
                            )
                        )

                # Retrieve the results and append them
                self.results = results
                u_j_d = np.concatenate(
                    [results[NofE][1] for NofE in range(n_cand_groups)]
                )

                # Check if all scores are inf
                if np.isinf(u_j_d).all() or np.isnan(u_j_d).all():
                    u_j_d = np.ones(len(u_j_d))

                # Get the expected value (mean) of the Utility score
                # for each cell
                if explore_method.lower() == "voronoi":
                    u_j_d = np.mean(u_j_d.reshape(-1, n_candidates), axis=1)

                # Normalize u_j_d
                # norm_u_j_d = u_j_d / np.nansum(np.abs(u_j_d))  # Possible solution
                norm_score_exploitation = u_j_d / np.sum(u_j_d)

            else:
                norm_score_exploitation = np.zeros((len(score_exploration)))

            # temp: Plot
            # dim = self.exp_design.x.shape[1]
            # if dim == 2:
            #     plotter(self.exp_design.x, allCandidates, explore_method)
            opt_type = "maximization"

        elif exploit_method.lower() == "varoptdesign":
            # ------- EXPLOITATION: VarOptDesign -------
            util_method = var

            # ------- Calculate Exoploration weight -------
            # Compute exploration weight based on trade off scheme
            explore_w, exploit_w = self.tradeoff_weights(
                tradeoff_scheme, old_ed_x, old_ed_y
            )
            print(
                f"\nweightExploration={explore_w:0.3f} "
                f"weightExploitation={exploit_w:0.3f}"
            )

            # Generate candidate samples from Exploration class
            n_measurement = old_ed_y[self.out_names[0]].shape[1]

            # Find sensitive region
            if util_method.lower() == "loocv":
                lc_error = self.meta_model.lc_error
                all_modified_loo = np.zeros(
                    (len(old_ed_x), len(self.out_names), n_measurement)
                )
                for y_idx, y_key in enumerate(self.out_names):
                    for idx, key in enumerate(lc_error[y_key].keys()):
                        all_modified_loo[:, y_idx, idx] = abs(lc_error[y_key][key])

                exploit_score = np.max(np.max(all_modified_loo, axis=1), axis=1)

            elif util_method in ["EIGF", "ALM"]:
                # ----- All other in  ['EIGF', 'ALM'] -----

                # Split the candidates in groups for multiprocessing
                if explore_method.lower() != "voronoi":
                    split_cand = np.array_split(all_candidates, n_cand_groups, axis=0)
                    good_sample_idx = range(n_cand_groups)
                else:
                    # Find indices of the Vornoi cells with samples
                    good_sample_idx = []
                    for idx in enumerate(explore.closest_points):
                        if len(explore.closest_points[idx]) != 0:
                            good_sample_idx.append(idx)
                    split_cand = explore.closest_points

                # Split the candidates in groups for multiprocessing
                args = []
                for index in good_sample_idx:
                    args.append((exploit_method, split_cand[index], index, var))

                # Multiprocessing
                with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
                    # With Pool.starmap_async()
                    results = pool.starmap_async(self.run_util_func, args).get()

                # Close the pool
                # pool.close()

                # Retrieve the results and append them
                if explore_method.lower() == "voronoi":
                    exploit_score = [
                        np.mean(results[k][1]) for k in range(len(good_sample_idx))
                    ]
                else:
                    exploit_score = np.concatenate(
                        [results[k][1] for k in range(len(good_sample_idx))]
                    )

            else:
                raise NameError("The requested utility function is not available.")

            # Total score - Normalize U_J_d
            norm_score_exploitation = exploit_score / np.sum(exploit_score)
            opt_type = "maximization"

        elif exploit_method.lower() == "alphabetic":
            # ------- EXPLOITATION: ALPHABETIC -------
            norm_score_exploitation = self.util_alph_opt_design(all_candidates, var)
            opt_type = "minimization"

        elif exploit_method.lower() == "space-filling":
            # ------- EXPLOITATION: SPACE-FILLING -------
            norm_score_exploitation = score_exploration
            exploit_w = 0
            opt_type = "maximization"

        else:
            raise NameError("The requested design method is not available.")

        # Accumulate all candidates and scores
        final_candidates = all_candidates
        total_score = (
            exploit_w * norm_score_exploitation + explore_w * score_exploration
        )

        # Choose the new training samples
        # If the total weights should be maximized
        if opt_type == "maximization":

            # ------- Select the best candidate -------
            # Find an optimal point subset to add to the initial design by
            # maximization of the utility score and taking care of NaN values
            temp = total_score.copy()
            # Since we are maximizing
            temp[np.isnan(total_score)] = -np.inf
            sorted_idxtotal_score = np.argsort(temp)[::-1]
            best_idx = sorted_idxtotal_score[:n_new_samples]
            if isinstance(best_idx, int):
                best_idx = [best_idx]

            # Select the requested number of samples
            if explore_method.lower() == "voronoi":
                x_new = np.zeros((n_new_samples, ndim))
                for i, idx in enumerate(best_idx):
                    x_can = explore.closest_points[idx]

                    # Calculate the maxmin score for the region of interest
                    new_samples, maxmin_score = explore.get_mc_samples(x_can)

                    # Select the requested number of samples
                    x_new[i] = new_samples[np.argmax(maxmin_score)]
            else:
                # Changed this from allCandiates to full set of candidates
                x_new = final_candidates[sorted_idxtotal_score[:n_new_samples]]

        # If the total weights should be maximized
        elif opt_type == "minimization":
            # find an optimal point subset to add to the initial design
            # by minimization of the phi
            sorted_idxtotal_score = np.argsort(total_score)

            # select the requested number of samples
            x_new = final_candidates[sorted_idxtotal_score[:n_new_samples]]

        print("\n")
        print(f"\nRun No. {old_ed_x.shape[0] + 1}")
        print("Xnew:\n", x_new)

        return x_new, None

    # -------------------------------------------------------------------------
    def tradeoff_weights(self, tradeoff_scheme, old_ed_x, old_ed_y):
        """
        Calculates weights for exploration scores based on the requested
        scheme: `None`, `equal`, `epsilon-decreasing` and `adaptive`.

        `None`: No exploration.
        `equal`: Same weights for exploration and exploitation scores.
        `epsilon-decreasing`: Start with more exploration and increase the
            influence of exploitation along the way with an exponential decay
            function
        `adaptive`: An adaptive method based on:
            Liu, Haitao, Jianfei Cai, and Yew-Soon Ong. "An adaptive sampling
            approach for Kriging metamodeling by maximizing expected prediction
            error." Computers & Chemical Engineering 106 (2017): 171-182.

        Parameters
        ----------
        tradeoff_scheme : string
            Trade-off scheme for exloration and exploitation scores.
        old_ed_x : array (n_samples, n_params)
            Old experimental design (training points).
        old_ed_y : dict
            Old model responses (targets).

        Returns
        -------
        exploration_weight : float
            Exploration weight.
        exploitation_weight: float
            Exploitation weight.

        """
        exploration_weight = None

        if tradeoff_scheme is None:
            exploration_weight = 0

        elif tradeoff_scheme.lower() == "equal":
            exploration_weight = 0.5

        elif tradeoff_scheme.lower() == "epsilon-decreasing":
            # epsilon-decreasing scheme
            # Start with more exploration and increase the influence of
            # exploitation along the way with an exponential decay function
            init_n_samples = self.exp_design.n_init_samples
            n_max_samples = self.exp_design.n_max_samples

            itr_number = self.exp_design.x.shape[0] - init_n_samples
            itr_number //= self.exp_design.n_new_samples

            tau2 = -(n_max_samples - init_n_samples - 1) / np.log(1e-8)
            exploration_weight = signal.windows.exponential(
                n_max_samples - init_n_samples, 0, tau2, False
            )[itr_number]

        elif tradeoff_scheme.lower() == "adaptive":

            # Extract itr_number
            init_n_samples = self.exp_design.n_init_samples
            # n_max_samples = self.exp_design.n_max_samples
            itr_number = self.exp_design.x.shape[0] - init_n_samples
            itr_number //= self.exp_design.n_new_samples

            if itr_number == 0:
                exploration_weight = 0.5
            else:
                # New adaptive trade-off according to Liu et al. (2017)
                # Mean squared error for last design point
                last_ed_x = old_ed_x[-1].reshape(1, -1)
                last_out_y, _ = self.meta_model.eval_metamodel(last_ed_x)
                pce_y = np.array(list(last_out_y.values()))[:, 0]
                y = np.array(list(old_ed_y.values()))[:, -1, :]
                mse_error = mean_squared_error(pce_y, y)

                # Mean squared CV - error for last design point
                metamod_y_prev = np.array(list(self._y_hat_prev.values()))[:, 0]
                mse_cv_error = mean_squared_error(metamod_y_prev, y)

                exploration_weight = min([0.5 * mse_error / mse_cv_error, 1])

        # Exploitation weight
        exploitation_weight = 1 - exploration_weight

        return exploration_weight, exploitation_weight

    # -------------------------------------------------------------------------
    def run_util_func(self, method, candidates, index, var=None, x_mc=None):
        """
        Runs the utility function based on the given method.

        Parameters
        ----------
        method : string
            Exploitation method: `VarOptDesign`, `BayesActDesign` and
            `BayesOptDesign`.
        candidates : array of shape (n_samples, n_params)
            All candidate parameter sets.
        index : int
            exp_design index.
        var : string, optional
            Utility function. The default is None.
        x_mc : array, optional
            Monte-Carlo samples. The default is None.

        Returns
        -------
        index : TYPE
            DESCRIPTION.
        List
            Scores.

        """

        if method.lower() == "varoptdesign":
            # u_j_d = self.util_var_based_design(candidates, index, var)
            u_j_d = np.zeros((candidates.shape[0]))
            for idx, x_can in tqdm(
                enumerate(candidates), ascii=True, desc="varoptdesign"
            ):
                u_j_d[idx] = self.util_var_based_design(x_can, index, var)

        elif method.lower() == "bayesactdesign":
            n_candidate = candidates.shape[0]
            u_j_d = np.zeros(n_candidate)
            # Evaluate all candidates
            y_can, std_can = self.meta_model.eval_metamodel(candidates)
            # loop through candidates
            for idx, x_can in tqdm(
                enumerate(candidates), ascii=True, desc="BAL Design"
            ):
                y_hat = {key: items[idx] for key, items in y_can.items()}
                std = {key: items[idx] for key, items in std_can.items()}

                u_j_d[idx] = self.util_bayesian_active_design(y_hat, std, var)

        elif method.lower() == "bayesoptdesign":
            n_candidate = candidates.shape[0]
            u_j_d = np.zeros(n_candidate)
            for idx, x_can in tqdm(
                enumerate(candidates), ascii=True, desc="OptBayesianDesign"
            ):
                u_j_d[idx] = self.util_bayesian_design(x_can, x_mc, var)
        return index, -1 * u_j_d

    # -------------------------------------------------------------------------

    def util_var_based_design(self, x_can, index, util_func="Entropy"):
        """
        Computes the exploitation scores based on:
        active learning MacKay(ALM) and active learning Cohn (ALC)
        Paper: Sequential Design with Mutual Information for Computer
        Experiments (MICE): Emulation of a Tsunami Model by Beck and Guillas
        (2016)

        Parameters
        ----------
        x_can : array of shape (n_samples, n_params)
            Candidate samples.
        index : int
            Model output index.
        util_func : string, optional
            Exploitation utility function. The default is 'Entropy'.

        Returns
        -------
        float
            Score.

        """
        meta_model = self.meta_model
        ed_x = self.exp_design.x
        out_dict_y = self.exp_design.y
        out_names = self.out_names

        # Run the meta_model for the candidate
        x_can = x_can.reshape(1, -1)
        y_metamod_can, std_metamod_can = meta_model.eval_metamodel(x_can)

        score = None
        if util_func.lower() == "alm":
            # ----- Entropy/MMSE/active learning MacKay(ALM)  -----
            # Compute perdiction variance of the old model
            can_pred_var = {key: std_metamod_can[key] ** 2 for key in out_names}

            var_metamod = np.zeros((len(out_names), x_can.shape[0]))
            for idx, key in enumerate(out_names):
                var_metamod[idx] = np.max(can_pred_var[key], axis=1)
            score = np.max(var_metamod, axis=0)

        elif util_func.lower() == "eigf":
            # ----- Expected Improvement for Global fit -----
            # Find closest EDX to the candidate
            distances = distance.cdist(ed_x, x_can, "euclidean")
            index = np.argmin(distances)

            # Compute perdiction error and variance of the old model
            pred_error = {key: y_metamod_can[key] for key in out_names}
            can_pred_var = {key: std_metamod_can[key] ** 2 for key in out_names}

            # Compute perdiction error and variance of the old model
            # Eq (5) from Liu et al.(2018)
            eigf_metamod = np.zeros((len(out_names), x_can.shape[0]))
            for idx, key in enumerate(out_names):
                residual = pred_error[key] - out_dict_y[key][int(index)]
                var = can_pred_var[key]
                eigf_metamod[idx] = np.max(residual**2 + var, axis=1)
            score = np.max(eigf_metamod, axis=0)

        return -1 * score  # -1 is for minimization instead of maximization

    # -------------------------------------------------------------------------
    def util_bayesian_active_design(self, y_hat, std, var="DKL"):
        """
        Computes scores based on Bayesian active design criterion (var).

        It is based on the following paper:
        Oladyshkin, Sergey, Farid Mohammadi, Ilja Kroeker, and Wolfgang Nowak.
        "Bayesian3 active learning for the gaussian process emulator using
        information theory." Entropy 22, no. 8 (2020): 890.

        Parameters
        ----------
        y_hat : unknown
        std : unknown
        var : string, optional
            BAL design criterion. The default is 'DKL'.

        Returns
        -------
        float
            Score.

        """
        if hasattr(self.model, "n_obs"):
            n_obs = self.model.n_obs
        else:
            n_obs = self.n_obs
        mc_size = 10000

        # Sample a distribution for a normal dist
        # with Y_mean_can as the mean and Y_std_can as std.
        y_mc, std_mc = {}, {}
        log_prior_likelihoods = np.zeros(mc_size)
        for key in list(y_hat):
            cov = np.diag(std[key] ** 2)
            # Allow for singular matrices
            rv = stats.multivariate_normal(
                mean=y_hat[key], cov=cov, allow_singular=True
            )
            y_mc[key] = rv.rvs(size=mc_size)
            log_prior_likelihoods += rv.logpdf(y_mc[key])
            std_mc[key] = np.zeros((mc_size, y_hat[key].shape[0]))

        #  Likelihood computation (Comparison of data and simulation
        #  results via PCE with candidate design)
        self.rej_sampler.prior_samples = np.random.rand(1, mc_size)[0]
        self.rej_sampler.log_prior_likelihoods = log_prior_likelihoods
        _ = self.rej_sampler.run_sampler(
            outputs=y_mc, std_outputs=std_mc, recalculate_loglik=True
        )
        _, inf_entropy = self.rej_sampler.calculate_valid_metrics(None)
        likelihoods = self.rej_sampler.likelihoods

        # Utility function Eq.2 in Ref. (2)
        # Posterior covariance matrix after observing data y
        # Kullback-Leibler Divergence (Sergey's paper)
        u_j_d = None
        if var.lower() == "dkl":
            # Calculate the correction factor for BME
            # BMECorrFactor = self.BME_Corr_Weight(PCE_SparseBayes_can,
            #                                      ObservationData, sigma2Dict)
            # BME += BMECorrFactor
            # Haun et al implementation
            # u_j_d = np.mean(np.log(Likelihoods[Likelihoods!=0])- logBME)
            u_j_d = self.rej_sampler.post_exp_likelihoods - self.rej_sampler.log_bme

        # Marginal log likelihood
        elif var.lower() == "bme":
            u_j_d = np.nanmean(likelihoods)

        # Entropy-based information gain
        elif var.lower() == "infentropy":
            u_j_d = inf_entropy * -1  # -1 for minimization

        # Bayesian information criterion
        elif var.lower() == "bic":
            # This function currently only supports PCE/aPCE
            if not hasattr(self.meta_model, "meta_model_type"):
                raise AttributeError(
                    "Sobol indices currently only support PCE-type models!"
                )
            if self.meta_model.meta_model_type.lower() not in ["pce", "apce"]:
                raise AttributeError(
                    "Sobol indices currently only support PCE-type models!"
                )

            coeffs = self.meta_model._coeffs_dict.values()
            n_model_params = max(len(v) for val in coeffs for v in val.values())
            u_j_d = -2 * np.log(np.nanmax(likelihoods)) + np.log(n_obs) * n_model_params

        # Akaike information criterion
        elif var.lower() == "aic":
            # This function currently only supports PCE/aPCE
            if not hasattr(self.meta_model, "meta_model_type"):
                raise AttributeError(
                    "Sobol indices currently only support PCE-type models!"
                )
            if self.meta_model.meta_model_type.lower() not in ["pce", "apce"]:
                raise AttributeError(
                    "Sobol indices currently only support PCE-type models!"
                )

            coeffs = self.meta_model._coeffs_dict.values()
            n_model_params = max(len(v) for val in coeffs for v in val.values())
            max_log_lik = np.log(np.nanmax(likelihoods))
            aic = -2 * max_log_lik + 2 * n_model_params
            # 2 * nModelParams * (nModelParams+1) / (n_obs-nModelParams-1)
            pen_term = 0
            u_j_d = 1 * (aic + pen_term)

        # Deviance information criterion
        elif var.lower() == "dic":
            # D_theta_bar = np.mean(-2 * Likelihoods)
            n_star_p = 0.5 * np.var(np.log(likelihoods[likelihoods != 0]))
            likelihoods_theta_mean = np.exp(
                self.rej_sampler.normpdf(y_hat, std_outputs=std)
            )
            dic = -2 * np.log(likelihoods_theta_mean) + 2 * n_star_p
            u_j_d = dic

        else:
            print("The algorithm you requested has not been implemented yet!")

        # Handle inf and NaN (replace by zero)
        if np.isnan(u_j_d) or u_j_d == -np.inf or u_j_d == np.inf:
            u_j_d = 0.0

        # Clear memory
        del likelihoods
        del y_mc
        del std_mc

        return -1 * u_j_d  # -1 is for minimization instead of maximization

    # -------------------------------------------------------------------------
    def util_bayesian_design(self, x_can, x_mc, var="DKL"):
        """
        Computes scores based on Bayesian sequential design criterion (var).

        Parameters
        ----------
        x_can : array of shape (n_samples, n_params)
            Candidate samples.
        x_mc : array
            Monte carlo samples
        var : string, optional
            Bayesian design criterion. The default is 'DKL'.

        Returns
        -------
        float
            Score.

        """

        # To avoid changes ub original aPCE object
        meta_model = self.meta_model
        out_names = self.out_names
        if x_can.ndim == 1:
            x_can = x_can.reshape(1, -1)

        # Compute the mean and std based on the meta_model
        # pce_means, pce_stds = self._compute_pce_moments(meta_model)
        if var.lower() == "alc":
            y_mc, y_mc_std = meta_model.eval_metamodel(x_mc)

        # Old Experimental design
        old_ed_x = self.exp_design.x
        old_ed_y = self.exp_design.y

        # Evaluate the PCE metamodels at the candidate location
        y_metamod_can, y_std_can = meta_model.eval_metamodel(x_can)
        metamod_can = deepcopy(meta_model)
        engine_can = deepcopy(self.engine)
        new_ed_x = np.vstack((old_ed_x, x_can))
        new_ed_y = {}
        for key in old_ed_y.keys():
            new_ed_y[key] = np.vstack((old_ed_y[key], y_metamod_can[key]))

        engine_can.exp_design.sampling_method = "user"
        engine_can.exp_design.x = new_ed_x
        engine_can.exp_design.y = new_ed_y

        # Train the model for the observed data using x_can
        engine_can.meta_model.input_obj.poly_coeffs_flag = False
        engine_can.train_normal(parallel=False)
        # engine_can.meta_model.fit(new_ed_x, new_ed_y)

        # Set the ExpDesign to its original values
        engine_can.exp_design.x = old_ed_x
        engine_can.exp_design.y = old_ed_y

        if var.lower() == "mi":
            # Mutual information based on Krause et al.
            # Adapted from Beck & Guillas (MICE) paper
            _, std_metamod_can = engine_can.meta_model.eval_metamodel(x_can)
            std_can = {key: std_metamod_can[key] for key in out_names}

            std_old = {key: y_std_can[key] for key in out_names}

            var_metamod = np.zeros((len(out_names)))
            for i, key in enumerate(out_names):
                var_metamod[i] = np.mean(std_old[key] ** 2 / std_can[key] ** 2)
            score = np.mean(var_metamod)

            return -1 * score

        if var.lower() == "alc":
            # Active learning based on Gramyc and Lee
            # Adaptive design and analysis of supercomputer experiments Techno-
            # metrics, 51 (2009), pp. 130–145.

            # Evaluate the meta_model at the given samples
            _, y_mc_std_can = engine_can.meta_model.eval_metamodel(x_mc)

            # Compute the score
            score = []
            for i, key in enumerate(out_names):
                pce_var = y_mc_std_can[key] ** 2
                pce_var_can = y_mc_std[key] ** 2
                score.append(np.mean(pce_var - pce_var_can, axis=0))
            score = np.mean(score)

            return -1 * score

        # ---------- Inner MC simulation for computing Utility Value ----------
        # Estimation of the integral via Monte Varlo integration
        mc_size = x_mc.shape[0]
        ess = 0
        while (ess > mc_size) or (ess < 1):

            # Enriching Monte Carlo samples if need be
            if ess != 0:
                x_mc = self.exp_design.generate_samples(mc_size, "random")

            # Evaluate the MetaModel at the given samples
            y_mc, std_mc = metamod_can.eval_metamodel(x_mc)

            # Rejection sampling
            self.rej_sampler.prior_samples = x_mc
            x_post = self.rej_sampler.run_sampler(
                outputs=y_mc,
                std_outputs=std_mc,
                consider_samplesize=True,
                recalculate_loglik=True,
            )
            ess = self.rej_sampler.ess

            # Enlarge sample size if it doesn't fulfill the criteria
            if (ess > mc_size) or (ess < 1):
                print(f"ESS={ess}, increasing the MC size.")
                mc_size *= 10

        # Validation metrics
        _, inf_entropy = self.rej_sampler.calculate_valid_metrics(self.exp_design)
        likelihoods = self.rej_sampler.likelihoods

        # -------------------- Utility functions --------------------
        # Utility function Eq.2 in Ref. (2)
        # Kullback-Leibler Divergence (Sergey's paper)
        u_j_d = None
        if var.lower() == "dkl":
            # Haun et al implementation
            u_j_d = np.mean(
                np.log(likelihoods[likelihoods != 0]) - self.rej_sampler.log_bme
            )

            # u_j_d = np.sum(G_n_m_all)
            # Ryan et al (2014) implementation
            # importanceWeights = Likelihoods[Likelihoods!=0]/np.sum(Likelihoods[Likelihoods!=0])
            # u_j_d = np.mean(importanceWeights*np.log(Likelihoods[Likelihoods!=0])) - logBME

            # u_j_d = postExpLikelihoods - logBME

        # Prior-based estimation of BME
        elif var.lower() == "bme":
            u_j_d = self.rej_sampler.log_bme

        # Bayes risk likelihood
        elif var.lower() == "bayesrisk":
            u_j_d = -1 * np.var(likelihoods)

        # Entropy-based information gain
        elif var.lower() == "infentropy":
            u_j_d = inf_entropy * -1  # -1 for minimization

        # D-Posterior-precision - covariance of the posterior parameters
        elif var.lower() == "dpp":
            u_j_d = -np.log(np.linalg.det(np.cov(x_post)))

        # A-Posterior-precision - trace of the posterior parameters
        elif var.lower() == "app":
            u_j_d = -np.log(np.trace(np.cov(x_post)))

        else:
            print("The algorithm you requested has not been implemented yet!")

        # Clear memory
        del likelihoods
        del y_mc
        del std_mc

        return -1 * u_j_d  # -1 is for minimization instead of maximization

    # -------------------------------------------------------------------------
    def dual_annealing(self, method, bounds, var, run_idx, verbose=False):
        """
        Exploration algorithm to find the optimum parameter space.

        Parameters
        ----------
        method : string
            Exploitation method: `VarOptDesign`, `BayesActDesign` and
            `BayesOptDesign`.
        bounds : list of tuples
            List of lower and upper boundaries of parameters.
        var : unknown
        run_idx : int
            Run number.
        verbose : bool, optional
            Print out a summary. The default is False.

        Returns
        -------
        run_idx : int
            Run number.
        array
            Optimial candidate.

        """

        max_func_itr = self.exp_design.max_func_itr

        res_global = None
        if method.lower() == "varoptdesign":
            res_global = opt.dual_annealing(
                self.util_var_based_design,
                bounds=bounds,
                args=(self.model, var),
                maxfun=max_func_itr,
            )

        elif method.lower() == "bayesoptdesign":
            res_global = opt.dual_annealing(
                self.util_bayesian_design,
                bounds=bounds,
                args=(self.model, var),
                maxfun=max_func_itr,
            )

        if verbose:
            print(
                f"Global minimum: xmin = {res_global.x}, "
                f"f(xmin) = {res_global.fun:.6f}, nfev = {res_global.nfev}"
            )

        return run_idx, res_global.x

    # -------------------------------------------------------------------------
    def util_alph_opt_design(self, candidates, var="D-Opt"):
        """
        Enriches the Experimental design with the requested alphabetic
        criterion based on exploring the space with number of sampling points.

        Ref: Hadigol, M., & Doostan, A. (2018). Least squares polynomial chaos
        expansion: A review of sampling strategies., Computer Methods in
        Applied Mechanics and Engineering, 332, 382-407.

        Arguments
        ---------
        candidates : int?
            Number of candidate points to be searched

        var : string
            Alphabetic optimality criterion

        Returns
        -------
        X_new : array of shape (1, n_params)
            The new sampling location in the input space.
        """

        # This function currently only supports PCE/aPCE
        if not hasattr(self.meta_model, "meta_model_type"):
            raise AttributeError(
                "Sobol indices currently only support PCE-type models!"
            )
        if self.meta_model.meta_model_type.lower() not in ["pce", "apce"]:
            raise AttributeError(
                "Sobol indices currently only support PCE-type models!"
            )

        n_candidate = candidates.shape[0]
        out_name = self.out_names[0]

        # Old Experimental design
        old_ed_x = self.exp_design.x

        # Suggestion: Go for the one with the highest LOO error
        # This is just a patch!
        scores = list(self.meta_model.loocv_score_dict["b_1"][out_name].values())
        mod_loo = [1 - score for score in scores]
        out_idx = np.argmax(mod_loo)

        # Initialize phi to save the criterion's values
        phi = np.zeros(n_candidate)

        # Patch
        basis_indices = self.meta_model._basis_dict["b_1"][out_name][
            "y_" + str(out_idx + 1)
        ]

        # ------ Old Psi ------------
        univ_p_val = self.meta_model.univ_basis_vals(old_ed_x)
        psi = create_psi(basis_indices, univ_p_val)

        # ------ New candidates (Psi_c) ------------
        # Assemble Psi_c
        univ_p_val_c = self.meta_model.univ_basis_vals(candidates)
        psi_c = create_psi(basis_indices, univ_p_val_c)

        for idx in range(n_candidate):

            # Include the new row to the original Psi
            psi_cand = np.vstack((psi, psi_c[idx]))

            # Information matrix
            psi_t_psi = np.dot(psi_cand.T, psi_cand)
            m = psi_t_psi / (len(old_ed_x) + 1)

            if 1e-12 < np.linalg.cond(psi_t_psi) < 1 / sys.float_info.epsilon:
                # faster
                inv_m = linalg.solve(m, sparse.eye(psi_t_psi.shape[0]).toarray())
            else:
                # stabler
                inv_m = np.linalg.pinv(m)

            # ---------- Calculate optimality criterion ----------
            # Optimality criteria according to Section 4.5.1 in Ref.

            # D-Opt
            if var.lower() == "d-opt":
                phi[idx] = (np.linalg.det(inv_m)) ** (1 / len(basis_indices))

            # A-Opt
            elif var.lower() == "a-opt":
                phi[idx] = np.trace(inv_m)

            # K-Opt
            elif var.lower() == "k-opt":
                phi[idx] = np.linalg.cond(m)

            else:
                raise Exception(
                    "The optimality criterion you requested has "
                    "not been implemented yet!"
                )

        return phi

    def _select_indexes(self, prior_samples, collocation_points):
        """
        This function will be used to check the user-input exploration samples,
        remove training points that were already used, and select the first mc_size
        samples that have not yet been used for training. It should also
        assign an exploration score of 0 to all samples.

        Parameters
        ----------
        prior_samples: array [mc_size, n_params]
            Pre-defined samples from the parameter space, out of which the
            sample sets should be extracted.
        collocation_points: [tp_size, n_params]
            array with training points which were already used to train
            the surrogate model, and should therefore
            not be re-explored.

        Returns
        -------
        array[self.mc_size,]
            With indexes of the new candidate parameter sets, to be read from
            the prior_samples array.

        """
        n_tp = collocation_points.shape[0]
        # a) get index of elements that have already been used
        aux1_ = np.where(
            (
                prior_samples[: self.mc_samples + n_tp, :]
                == collocation_points[:, None]
            ).all(-1)
        )[1]
        # b) give each element in the prior a True if it has not been used before
        aux2_ = np.invert(
            np.in1d(
                np.arange(prior_samples[: self.mc_samples + n_tp, :].shape[0]), aux1_
            )
        )
        # c) Select the first d_size_bal elements in prior_sample that have not been used before
        al_unique_index = np.arange(
            prior_samples[: self.mc_samples + n_tp, :].shape[0]
        )[aux2_]
        al_unique_index = al_unique_index[: self.mc_samples]

        return al_unique_index
