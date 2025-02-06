#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Collection of postprocessing functions into a class.
"""

import os
from itertools import combinations, cycle
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib.offsetbox import AnchoredText
from matplotlib.patches import Patch

from bayesvalidrox.surrogate_models.supplementary import root_mean_squared_error

plt.style.use(os.path.join(os.path.split(__file__)[0], "../", "bayesvalidrox.mplstyle"))


class PostProcessing:
    """
    This class provides post-processing functions for the trained metamodels.

    Parameters
    ----------
    engine : obj
        Trained Engine object, is expected to contain a trained MetaModel object.
    name : string
        Name of the PostProcessing object to be used for saving the generated files.
        The default is 'calib'.
    out_dir : string
        Output directory in which the PostProcessing results are placed.
        The results are contained in a subfolder '/Outputs_PostProcessing_name'
        The default is ''.
    out_format : string
        Format of the saved plots. Supports 'png' and 'pdf'. The default is 'pdf'.

    Raises
    ------
    AttributeError
        `engine` must be trained.

    """

    def __init__(self, engine, name="calib", out_dir="", out_format="pdf"):
        # PostProcessing only available for trained engines
        if not engine.trained:
            raise AttributeError(
                "PostProcessing can only be performed on trained engines."
            )

        if not engine.meta_model:
            raise AttributeError(
                "PostProcessing can only be performed on engines with a trained MetaModel."
            )

        self.engine = engine
        self.name = name
        self.out_format = out_format
        self.par_names = self.engine.exp_design.par_names
        self.x_values = self.engine.exp_design.x_values

        self.out_dir = f"./{out_dir}/Outputs_PostProcessing_{self.name}/"

        # Open a pdf for the plots
        if not os.path.exists(self.out_dir):
            os.makedirs(self.out_dir)

        # Initialize attributes
        self.plot_type = ""
        self.xlabel = "Time [s]"
        self.mc_reference = None
        self.sobol = None
        self.totalsobol = None
        self.valid_error = None
        self.rmse = None
        self.model_out_dict = {}
        self.means = None
        self.stds = None

        self.out_dir = f"./{out_dir}/Outputs_PostProcessing_{self.name}/"

        # Open a pdf for the plots
        if not os.path.exists(self.out_dir):
            os.makedirs(self.out_dir)

        # Initialize attributes
        self.mc_reference = None
        self.total_sobol = None
        self.valid_error = None
        self.rmse = None
        self.model_out_dict = {}
        self.means = None
        self.stds = None

    # -------------------------------------------------------------------------
    def plot_moments(self, plot_type: str = "line"):
        """
        Plots the moments in a user defined output format (standard is pdf) in the directory
        `Outputs_PostProcessing`.

        Parameters
        ----------
        plot_type : str, optional
            Supports 'bar' for barplots and 'line'
            for lineplots The default is `line`.

        Raises
        ------
        AttributeError
            Plot type must be 'bar' or 'line'.

        Returns
        -------
        pce_means: dict
            Mean of the model outputs.
        pce_means: dict
            Standard deviation of the model outputs.

        """
        if plot_type not in ["bar", "line"]:
            raise AttributeError("The wanted plot-type is not supported.")
        bar_plot = bool(plot_type == "bar")
        meta_model_type = self.engine.meta_model.meta_model_type

        # Read Monte-Carlo reference
        self.mc_reference = self.engine.model.read_observation("mc_ref")

        # Compute the moments with the PCEModel object
        self.means, self.stds = self.engine.meta_model.calculate_moments()

        # Plot the best fit line
        for key in self.engine.out_names:
            fig, ax = plt.subplots(nrows=1, ncols=2)

            # Extract mean and std
            mean_data = self.means[key]
            std_data = self.stds[key]

            # Plot: bar plot or line plot
            if bar_plot:
                ax[0].bar(
                    list(map(str, self.x_values)), mean_data, color="b", width=0.25
                )
                ax[1].bar(
                    list(map(str, self.x_values)), std_data, color="b", width=0.25
                )
                ax[0].legend(labels=[meta_model_type])
                ax[1].legend(labels=[meta_model_type])
            else:
                ax[0].plot(
                    self.x_values,
                    mean_data,
                    lw=3,
                    color="k",
                    marker="x",
                    label=meta_model_type,
                )
                ax[1].plot(
                    self.x_values,
                    std_data,
                    lw=3,
                    color="k",
                    marker="x",
                    label=meta_model_type,
                )

            if self.mc_reference is not None:
                if bar_plot:
                    ax[0].bar(
                        list(map(str, self.x_values)),
                        self.mc_reference["mean"],
                        color="r",
                        width=0.25,
                    )
                    ax[1].bar(
                        list(map(str, self.x_values)),
                        self.mc_reference["std"],
                        color="r",
                        width=0.25,
                    )
                    ax[0].legend(labels=[meta_model_type])
                    ax[1].legend(labels=[meta_model_type])
                else:
                    ax[0].plot(
                        self.x_values,
                        self.mc_reference["mean"],
                        lw=3,
                        marker="x",
                        color="r",
                        label="Ref.",
                    )
                    ax[1].plot(
                        self.x_values,
                        self.mc_reference["std"],
                        lw=3,
                        marker="x",
                        color="r",
                        label="Ref.",
                    )

            # Label the axes and provide a title
            ax[0].set_xlabel(self.xlabel)
            ax[1].set_xlabel(self.xlabel)
            ax[0].set_ylabel(key)
            ax[1].set_ylabel(key)

            # Provide a title
            ax[0].set_title("Mean of " + key)
            ax[1].set_title("Std of " + key)

            if not bar_plot:
                ax[0].legend(loc="best")
                ax[1].legend(loc="best")
            plt.tight_layout()
            fig.savefig(
                f"{self.out_dir}Mean_Std_PCE_{key}.{self.out_format}",
                bbox_inches="tight",
            )

        return self.means, self.stds

    # -------------------------------------------------------------------------
    def valid_metamodel(self, n_samples=1, samples=None, model_out_dict=None) -> None:
        """
        Evaluates and plots the meta model and the PCEModel outputs for the
        given number of samples or the given samples.

        Parameters
        ----------
        n_samples : int, optional
            Number of samples to be evaluated. The default is 1.
        samples : array of shape (n_samples, n_params), optional
            Samples to be evaluated. The default is None.
        model_out_dict: dict
            The model runs using the samples provided.

        Returns
        -------
        None

        """
        if samples is None:
            samples = self.engine.exp_design.generate_samples(
                n_samples, sampling_method="random"
            )
        else:
            n_samples = samples.shape[0]

        if model_out_dict is None:
            model_out_dict, _ = self.engine.model.run_model_parallel(
                samples, key_str="valid"
            )

        out_mean, out_std = self.engine.eval_metamodel(samples)

        self._plot_validation_multi(out_mean, out_std, model_out_dict)

        # Zip the subdirectories
        self.engine.model.zip_subdirs(
            f"{self.engine.model.name}valid", f"{self.engine.model.name}valid_"
        )

    # -------------------------------------------------------------------------
    def check_accuracy(self, n_samples=None, samples=None, outputs=None) -> None:
        """
        Checks accuracy of the metamodel by computing the root mean square
        error and validation error for all outputs.

        Parameters
        ----------
        n_samples : int, optional
            Number of samples. The default is None.
        samples : array of shape (n_samples, n_params), optional
            Parameter sets to be checked. The default is None.
        outputs : dict, optional
            Output dictionary with model outputs for all given output types in
            `engine.out_names`. The default is None.

        Raises
        ------
        AttributeError
            When neither n_samples nor samples are provided.

        Returns
        -------
        None

        """
        # Set the number of samples
        if samples is None and n_samples is None:
            raise AttributeError(
                "Please provide either samples or pass the number of samples!"
            )
        n_samples = samples.shape[0] if samples is not None else n_samples

        # Generate random samples if necessary
        if samples is None:
            samples = self.engine.exp_design.generate_samples(
                n_samples, sampling_method="random"
            )

        # Run the original model with the generated samples
        if outputs is None:
            outputs, _ = self.engine.model.run_model_parallel(samples, key_str="valid")

        # Run the PCE model with the generated samples
        metamod_outputs, _ = self.engine.eval_metamodel(samples)

        self.rmse = {}
        self.valid_error = {}
        # Loop over the keys and compute RMSE error.
        for key in self.engine.out_names:
            # Root mena square
            self.rmse[key] = root_mean_squared_error(outputs[key], metamod_outputs[key])
            # Validation error
            self.valid_error[key] = (self.rmse[key] ** 2) / np.var(
                outputs[key], ddof=1, axis=0
            )

            # Print a report table
            print(f"\n>>>>> Errors of {key} <<<<<")
            print("\nIndex  |  RMSE   |  Validation Error")
            print("-" * 35)
            print(
                "\n".join(
                    f"{i+1}  |  {k:.3e}  |  {j:.3e}"
                    for i, (k, j) in enumerate(
                        zip(self.rmse[key], self.valid_error[key])
                    )
                )
            )
        # Save error dicts in meta_model object
        self.engine.meta_model.rmse = self.rmse
        self.engine.meta_model.valid_error = self.valid_error

    # -------------------------------------------------------------------------
    def plot_seq_design_diagnostics(self, ref_bme_kld=None) -> None:
        """
        Plots the Bayesian Model Evidence (BME) and Kullback-Leibler divergence
        (KLD) for the sequential design.

        Parameters
        ----------
        ref_bme_kld : array, optional
            Reference BME and KLD . The default is `None`.

        Returns
        -------
        None

        """
        engine = self.engine
        n_init_samples = engine.exp_design.n_init_samples
        n_total_samples = engine.exp_design.n_max_samples

        newpath = f"{self.out_dir}/seq_design_diagnostics/"
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        plot_list = [
            "Modified LOO error",
            "Validation error",
            "KLD",
            "BME",
            "RMSEMean",
            "RMSEStd",
            "Hellinger distance",
        ]
        seq_list = [
            engine.seq_modified_loo,
            engine.seq_valid_error,
            engine.seq_kld,
            engine.seq_bme,
            engine.seq_rmse_mean,
            engine.seq_rmse_std,
            engine.seq_dist_hellinger,
        ]

        markers = ("x", "o", "d", "*", "+")
        colors = ("k", "darkgreen", "b", "navy", "darkred")

        # Plot the evolution of the diagnostic criteria of the
        # Sequential Experimental Design.

        for plotidx, plot in enumerate(plot_list):
            fig, ax = plt.subplots()
            seq_dict = seq_list[plotidx]
            name_util = list(seq_dict.keys())
            if len(name_util) == 0:
                continue

            # Box plot when Replications have been detected.
            if any(int(name.split("rep_", 1)[1]) > 1 for name in name_util):
                sorted_seq_opt = {}
                n_reps = engine.exp_design.n_replication

                # Handle if only one UtilityFunction is provided
                if not isinstance(engine.exp_design.util_func, list):
                    util_funcs = [engine.exp_design.util_func]
                else:
                    util_funcs = engine.exp_design.util_func

                for util in util_funcs:
                    sorted_seq = {}
                    n_runs = min(
                        seq_dict[f"{util}_rep_{i + 1}"].shape[0] for i in range(n_reps)
                    )

                    for run_idx in range(n_runs):
                        values = []
                        for key in seq_dict.keys():
                            if util in key:
                                values.append(seq_dict[key][run_idx].mean())
                        sorted_seq["SeqItr_" + str(run_idx)] = np.array(values)
                    sorted_seq_opt[util] = sorted_seq

                # BoxPlot
                def draw_plot(data, labels, edge_color, fill_color, idx):
                    pos = labels - (idx - 1)
                    bp = plt.boxplot(
                        data,
                        positions=pos,
                        labels=labels,
                        patch_artist=True,
                        sym="",
                        widths=0.75,
                    )
                    elements = [
                        "boxes",
                        "whiskers",
                        "fliers",
                        "means",
                        "medians",
                        "caps",
                    ]
                    for element in elements:
                        plt.setp(bp[element], color=edge_color[idx])

                    for patch in bp["boxes"]:
                        patch.set(facecolor=fill_color[idx])

                if engine.exp_design.n_new_samples != 1:
                    step1 = engine.exp_design.n_new_samples
                    step2 = 1
                else:
                    step1 = 5
                    step2 = 5
                edge_color = ["red", "blue", "green"]
                fill_color = ["tan", "cyan", "lightgreen"]
                plot_label = plot
                # Plot for different Utility Functions
                for idx, util in enumerate(util_funcs):
                    all_errors = np.empty((n_reps, 0))

                    for key in list(sorted_seq_opt[util].keys()):
                        errors = sorted_seq_opt.get(util, {}).get(key)[:, None]
                        all_errors = np.hstack((all_errors, errors))

                    # Special cases for BME and KLD
                    if plot in ["KLD", "BME"]:
                        # BME convergence if refBME is provided
                        if ref_bme_kld is not None:
                            ref_value = None
                            if plot == "BME":
                                ref_value = ref_bme_kld[0]
                                plot_label = r"BME/BME$^{Ref.}$"
                            if plot == "KLD":
                                ref_value = ref_bme_kld[1]
                                plot_label = (
                                    "$D_{KL}[p(\\theta|y_*),p(\\theta)]"
                                    " / D_{KL}^{Ref.}[p(\\theta|y_*), "
                                    "p(\\theta)]$"
                                )

                            # Difference between BME/KLD and the ref. values
                            all_errors = np.divide(
                                all_errors, np.full((all_errors.shape), ref_value)
                            )

                            # Plot baseline for zero, i.e. no difference
                            plt.axhline(y=1.0, xmin=0, xmax=1, c="green", ls="--", lw=2)

                    # Plot each UtilFuncs
                    labels = np.arange(n_init_samples, n_total_samples + 1, step1)
                    draw_plot(
                        all_errors[:, ::step2], labels, edge_color, fill_color, idx
                    )

                plt.xticks(labels, labels)
                # Set the major and minor locators
                ax.xaxis.set_major_locator(ticker.AutoLocator())
                ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
                ax.xaxis.grid(True, which="major", linestyle="-")
                ax.xaxis.grid(True, which="minor", linestyle="--")

                # Legend
                legend_elements = []
                for idx, util in enumerate(util_funcs):
                    legend_elements.append(
                        Patch(
                            facecolor=fill_color[idx],
                            edgecolor=edge_color[idx],
                            label=util,
                        )
                    )
                plt.legend(handles=legend_elements[::-1], loc="best")

                if plot not in ["BME", "KLD"]:
                    plt.yscale("log")
                plt.autoscale(True)
                plt.xlabel("\\# of training samples")
                plt.ylabel(plot_label)
                plt.title(plot)

                # save the current figure
                plot_name = plot.replace(" ", "_")
                fig.savefig(
                    f"./{newpath}/seq_{plot_name}.{self.out_format}",
                    bbox_inches="tight",
                )
                # Destroy the current plot
                plt.close()
                # Save arrays into files
                f = open(f"./{newpath}/seq_{plot_name}.txt", "w")
                f.write(str(sorted_seq_opt))
                f.close()
            else:
                for idx, name in enumerate(name_util):
                    seq_values = seq_dict[name]
                    if engine.exp_design.n_new_samples != 1:
                        step = engine.exp_design.n_new_samples
                    else:
                        step = 1
                    x_idx = np.arange(n_init_samples, n_total_samples + 1, step)
                    if n_total_samples not in x_idx:
                        x_idx = np.hstack((x_idx, n_total_samples))

                    if plot in ["KLD", "BME"]:
                        # BME convergence if refBME is provided
                        if ref_bme_kld is not None:
                            if plot == "BME":
                                ref_value = ref_bme_kld[0]
                                plot_label = r"BME/BME$^{Ref.}$"
                            if plot == "KLD":
                                ref_value = ref_bme_kld[1]
                                plot_label = (
                                    "$D_{KL}[p(\\theta|y_*),p(\\theta)]"
                                    " / D_{KL}^{Ref.}[p(\\theta|y_*), "
                                    "p(\\theta)]$"
                                )

                            # Difference between BME/KLD and the ref. values
                            values = np.divide(
                                seq_values, np.full((seq_values.shape), ref_value)
                            )

                            # Plot baseline for zero, i.e. no difference
                            plt.axhline(y=1.0, xmin=0, xmax=1, c="green", ls="--", lw=2)

                            # Set the limits
                            plt.ylim([1e-1, 1e1])

                            # Create the plots
                            plt.semilogy(
                                x_idx,
                                values,
                                marker=markers[idx],
                                color=colors[idx],
                                ls="--",
                                lw=2,
                                label=name.split("_rep", 1)[0],
                            )
                        else:
                            plot_label = plot

                            # Create the plots
                            plt.plot(
                                x_idx,
                                seq_values,
                                marker=markers[idx],
                                color=colors[idx],
                                ls="--",
                                lw=2,
                                label=name.split("_rep", 1)[0],
                            )

                    else:
                        plot_label = plot
                        seq_values = np.nan_to_num(seq_values)

                        # Plot the error evolution for each output
                        plt.semilogy(
                            x_idx,
                            seq_values.mean(axis=1),
                            marker=markers[idx],
                            ls="--",
                            lw=2,
                            color=colors[idx],
                            label=name.split("_rep", 1)[0],
                        )

                # Set the major and minor locators
                ax.xaxis.set_major_locator(ticker.AutoLocator())
                ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
                ax.xaxis.grid(True, which="major", linestyle="-")
                ax.xaxis.grid(True, which="minor", linestyle="--")

                ax.tick_params(
                    axis="both", which="major", direction="in", width=3, length=10
                )
                ax.tick_params(
                    axis="both", which="minor", direction="in", width=2, length=8
                )
                plt.xlabel("Number of runs")
                plt.ylabel(plot_label)
                plt.title(plot)
                plt.legend(frameon=True)

                # save the current figure
                plot_name = plot.replace(" ", "_")
                fig.savefig(
                    f"./{newpath}/seq_{plot_name}.{self.out_format}",
                    bbox_inches="tight",
                )
                # Destroy the current plot
                plt.close()

                # ---------------- Saving arrays into files ---------------
                np.save(f"./{newpath}/seq_{plot_name}.npy", seq_values)

    # -------------------------------------------------------------------------
    def sobol_indices(self, plot_type: str = "line", save: bool = True):
        """
        Visualizes and writes out Sobol' and Total Sobol' indices of the trained metamodel.
        One file is created for each index and output key.

        Parameters
        ----------
        plot_type : str, optional
            Plot type, supports 'line' for lineplots and 'bar' for barplots.
            The default is `line`.
            Bar chart can be selected by `bar`.
        save : bool, optional
            Write out the inidces as csv files if set to True. The default
            is True.

        Raises
        ------
        AttributeError
            MetaModel in given Engine needs to be of type 'pce' or 'apce'.
        AttributeError
            Plot-type must be 'line' or 'bar'.

        Returns
        -------
        sobol_all : dict
            All possible Sobol' indices for the given metamodel.
        total_sobol_all : dict
            All Total Sobol' indices for the given metamodel.

        """
        # This function currently only supports PCE/aPCE
        metamod = self.engine.meta_model
        if not hasattr(metamod, "meta_model_type"):
            raise AttributeError("Sobol indices only support PCE-type models!")
        if metamod.meta_model_type.lower() not in ["pce", "apce"]:
            raise AttributeError("Sobol indices only support PCE-type models!")

        if plot_type not in ["line", "bar"]:
            raise AttributeError("The wanted plot type is not supported.")

        # Extract the necessary variables
        max_order = np.max(metamod.pce_deg)
        outputs = self.engine.out_names
        if metamod.sobol is None:
            metamod.calculate_sobol(y_train=self.engine.exp_design.y)
        sobol_all, total_sobol_all = metamod.sobol, metamod.total_sobol
        self.sobol = sobol_all
        self.totalsobol = total_sobol_all

        # Save indices
        if save:
            for _, output in enumerate(outputs):
                total_sobol = total_sobol_all[output]
                np.savetxt(
                    f"{self.out_dir}totalsobol_" + output.replace("/", "_") + ".csv",
                    total_sobol.T,
                    delimiter=",",
                    header=",".join(self.par_names),
                    comments="",
                )

                for i_order in range(1, max_order + 1):
                    sobol = sobol_all[i_order][output][0]
                    np.savetxt(
                        f"{self.out_dir}sobol_{i_order}_"
                        + output.replace("/", "_")
                        + ".csv",
                        sobol.T,
                        delimiter=",",
                        header=",".join(self.par_names),
                        comments="",
                    )

        # Plot Sobol' indices
        self.plot_type = plot_type
        for i_order in range(1, max_order + 1):
            par_names_i = (
                list(combinations(self.par_names, i_order))
                if (i_order != 1)
                else self.par_names
            )
            self.plot_sobol(par_names_i, outputs, sobol_type="sobol", i_order=i_order)
        self.plot_sobol(self.par_names, outputs, sobol_type="totalsobol")

        return sobol_all, total_sobol_all

    def plot_sobol(
        self,
        par_names: list,
        outputs: list,
        sobol_type: str = "sobol",
        i_order: int = 0,
    ) -> None:
        """
        Generate plots for each output in the given set of Sobol' indices.

        Parameters
        ----------
        par_names : list
            Parameter names for each Sobol' index.
        outputs : list
            Output names to be plotted.
        sobol_type : string, optional
            Type of Sobol' indices to visualize. Can be either
            'sobol' or 'totalsobol'. The default is 'sobol'.
        i_order : int, optional
            Order of Sobol' index that should be plotted.
            This parameter is only applied for sobol_type = 'sobol'.
            The default is 0.

        Returns
        -------
        None

        """
        sobol = None
        if sobol_type == "sobol":
            sobol = self.sobol[i_order]
        if sobol_type == "totalsobol":
            sobol = self.totalsobol

        for _, output in enumerate(outputs):
            x = (
                self.x_values[output]
                if isinstance(self.x_values, dict)
                else self.x_values
            )
            sobol_ = sobol[output]
            if sobol_type == "sobol":
                sobol_3d = sobol[output]
                sobol_ = sobol_[0]
            if sobol_type == "totalsobol" and len(sobol_.shape) == 2:
                sobol_3d = np.array([sobol_])

            # Compute quantiles
            q_5 = np.quantile(sobol_3d, q=0.05, axis=0)
            q_97_5 = np.quantile(sobol_3d, q=0.975, axis=0)

            if self.plot_type == "bar":
                fig = plt.figure()
                ax = fig.add_axes([0, 0, 1, 1])
                dict1 = {self.xlabel: x}
                dict2 = dict(zip(par_names, sobol_))

                df = pd.DataFrame({**dict1, **dict2})
                df.plot(
                    x=self.xlabel,
                    y=par_names,
                    kind="bar",
                    ax=ax,
                    rot=0,
                    colormap="Dark2",
                    yerr=q_97_5 - q_5,
                )
                if sobol_type == "sobol":
                    ax.set_ylabel("Sobol indices, $S^T$")
                elif sobol_type == "totalsobol":
                    ax.set_ylabel("Total Sobol indices, $S^T$")

            else:
                fig = plt.figure()
                ax = fig.add_axes([0, 0, 1, 1])
                for i, sobol_indices in enumerate(sobol_):
                    plt.plot(
                        x,
                        sobol_indices,
                        label=par_names[i],
                        marker="x",
                        lw=2.5,
                    )
                    plt.fill_between(x, q_5[i], q_97_5[i], alpha=0.15)

                if sobol_type == "sobol":
                    ax.set_ylabel("Sobol indices, $S^T$")
                elif sobol_type == "totalsobol":
                    ax.set_ylabel("Total Sobol indices, $S^T$")
                plt.xlabel(self.xlabel)
                plt.legend(loc="best", frameon=True)

            if sobol_type == "sobol":
                plt.title(f"{i_order} order Sobol' indices of {output}")
                fig.savefig(
                    f"{self.out_dir}Sobol_indices_{i_order}_{output}.{self.out_format}",
                    bbox_inches="tight",
                )
            elif sobol_type == "totalsobol":
                plt.title(f"Total Sobol' indices of {output}")
                fig.savefig(
                    f"{self.out_dir}TotalSobol_indices_{output}.{self.out_format}",
                    bbox_inches="tight",
                )
            plt.clf()

    # -------------------------------------------------------------------------
    def check_reg_quality(
        self, n_samples: int = 1000, samples=None, outputs: dict = None
    ) -> None:
        """
        Checks the quality of the metamodel for single output models based on:
        https://towardsdatascience.com/how-do-you-check-the-quality-of-your-regression-model-in-python-fa61759ff685

        Parameters
        ----------
        n_samples : int, optional
            Number of parameter sets to use for the check. The default is 1000.
        samples : array of shape (n_samples, n_params), optional
            Parameter sets to use for the check. The default is None.
        outputs : dict, optional
            Output dictionary with model outputs for all given output types in
            `engine.out_names`. The default is None.

        Returns
        -------
        None

        """
        if samples is None:
            samples = self.engine.exp_design.generate_samples(
                n_samples, sampling_method="random"
            )
        else:
            n_samples = samples.shape[0]

        # Evaluate the original and the surrogate model
        y_val = outputs
        if y_val is None:
            y_val, _ = self.engine.model.run_model_parallel(samples, key_str="valid")
        y_metamod_val, _ = self.engine.eval_metamodel(samples=samples)

        # Fit the data(train the model)
        for key in y_metamod_val.keys():
            residuals = y_val[key] - y_metamod_val[key]

            # ------ Residuals vs. predicting variables ------
            # Check the assumptions of linearity and independence
            for i, par in enumerate(self.engine.exp_design.par_names):
                plt.scatter(x=samples[:, i], y=residuals, color="blue", edgecolor="k")
                plt.title(f"{key}: Residuals vs. {par}")
                plt.grid(True)
                plt.hlines(
                    y=0,
                    xmin=min(samples[:, i]) * 0.9,
                    xmax=max(samples[:, i]) * 1.1,
                    color="red",
                    lw=3,
                    linestyle="--",
                )
                plt.xlabel(par)
                plt.ylabel("Residuals")
                plt.savefig(
                    f"./{self.out_dir}/Residuals_vs_Par_{i+1}.{self.out_format}",
                    bbox_inches="tight",
                )
                plt.close()

            # ------ Fitted vs. residuals ------
            # Check the assumptions of linearity and independence
            for i in range(y_metamod_val[key].shape[0]):
                plt.scatter(
                    x=y_metamod_val[key][i, :],
                    y=residuals[i, :],
                    color="blue",
                    edgecolor="k",
                )
            plt.title(f"{key}: Residuals vs. fitted values")
            plt.grid(True)
            plt.hlines(
                y=0,
                xmin=min(y_val[key]) * 0.9,
                xmax=max(y_val[key]) * 1.1,
                color="red",
                lw=3,
                linestyle="--",
            )
            plt.xlabel(key)
            plt.ylabel("Residuals")
            plt.savefig(
                f"./{self.out_dir}/Fitted_vs_Residuals.{self.out_format}",
                bbox_inches="tight",
            )
            plt.close()

            # ------ Histogram of normalized residuals ------
            resid_pearson = residuals / (max(residuals) - min(residuals))
            plt.hist(resid_pearson, bins=20, edgecolor="k")
            plt.ylabel("Count")
            plt.xlabel("Normalized residuals")
            plt.title(f"{key}: Histogram of normalized residuals")

            # Normality (Shapiro-Wilk) test of the residuals
            ax = plt.gca()
            _, p = stats.shapiro(residuals)
            if p < 0.01:
                ann_text = "The residuals seem to come from a Gaussian Process."
            else:
                ann_text = "The normality assumption may not hold."
            at = AnchoredText(
                ann_text, prop={"size": 30}, frameon=True, loc="upper left"
            )
            at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
            ax.add_artist(at)
            plt.savefig(
                f"./{self.out_dir}/Hist_NormResiduals.{self.out_format}",
                bbox_inches="tight",
            )
            plt.close()

            # ------ Q-Q plot of the normalized residuals ------
            plt.figure()
            stats.probplot(residuals[:, 0], plot=plt)
            plt.xticks()
            plt.yticks()
            plt.xlabel("Theoretical quantiles")
            plt.ylabel("Sample quantiles")
            plt.title(f"{key}: Q-Q plot of normalized residuals")
            plt.grid(True)
            plt.savefig(
                f"./{self.out_dir}/QQPlot_NormResiduals.{self.out_format}",
                bbox_inches="tight",
            )
            plt.close()

    # -------------------------------------------------------------------------
    def plot_metamodel_3d(self, n_samples=10):
        """
        Visualize the results of a MetaModel as a 3D surface over two input
        parameters.

        Parameters
        ----------
        n_samples : int
            Number of samples that are used to generate the 3D plot.

        Raises
        ------
        AttributeError
            This function is only applicable if the MetaModel input dimension is 2.

        Returns
        -------
        None

        """
        if self.engine.exp_design.ndim != 2:
            raise AttributeError(
                "This function is only applicable if the MetaModel input dimension is 2."
            )
        samples = self.engine.exp_design.generate_samples(n_samples)
        samples = np.sort(np.sort(samples, axis=1), axis=0)
        mean, _ = self.engine.eval_metamodel(samples=samples)

        title = "MetaModel" if self.engine.emulator else "Model"
        x, y = np.meshgrid(samples[:, 0], samples[:, 1])
        for name in self.engine.out_names:
            for t in range(mean[name].shape[1]):
                fig = plt.figure()
                ax = plt.axes(projection="3d")
                ax.plot_surface(
                    x,
                    y,
                    np.atleast_2d(mean[name][:, t]),
                    rstride=1,
                    cstride=1,
                    cmap="viridis",
                    edgecolor="none",
                )
                ax.set_title(title)
                ax.set_xlabel("$x_1$")
                ax.set_ylabel("$x_2$")
                ax.set_zlabel("$f(x_1,x_2)$")

                plt.grid()
                fig.savefig(
                    f"./{self.out_dir}/3DPlot_{title}_{name}{t}.{self.out_format}",
                    bbox_inches="tight",
                )
                plt.close(fig)

    # -------------------------------------------------------------------------
    def _plot_validation_multi(self, out_mean, out_std, model_out):
        """
        Plots outputs for visual comparison of metamodel outputs with that of
        the (full) multioutput original model

        Parameters
        ----------
        out_mean : dict
            MetaModel mean outputs.
        out_std : dict
            MetaModel stdev outputs.
        model_out : dict
            Model outputs.

        Raises
        ------
        AttributeError: This evaluation only support PCE-type models!

        Returns
        -------
        None

        """
        # List of markers and colors
        color = cycle((["b", "g", "r", "y", "k"]))
        marker = cycle(("x", "d", "+", "o", "*"))
        metamod_name = self.engine.meta_model.meta_model_type.lower()

        # Plot the model vs PCE model
        fig = plt.figure()
        for _, key in enumerate(self.engine.out_names):
            y_val = out_mean[key]
            y_val_std = out_std[key]
            y_val = model_out[key]

            for idx in range(y_val.shape[0]):
                plt.plot(
                    self.x_values,
                    y_val[idx],
                    color=next(color),
                    marker=next(marker),
                    label="$Y_{%s}^M$" % (idx + 1),
                )
                plt.plot(
                    self.x_values,
                    y_val[idx],
                    color=next(color),
                    marker=next(marker),
                    linestyle="--",
                    label=f"$Y_{{{idx+1}}}^{{{metamod_name}}}$",
                )
                plt.fill_between(
                    self.x_values,
                    y_val[idx] - 1.96 * y_val_std[idx],
                    y_val[idx] + 1.96 * y_val_std[idx],
                    color=next(color),
                    alpha=0.15,
                )

            # Calculate the RMSE
            rmse = root_mean_squared_error(y_val, y_val)
            r_2 = r2_score(y_val[idx].reshape(-1, 1), y_val[idx].reshape(-1, 1))

            plt.annotate(
                f"RMSE = {rmse}\n $R^2$ = {r_2:.3f}",
                xy=(0.85, 0.1),
                xycoords="axes fraction",
            )
            plt.ylabel(key)
            plt.xlabel(self.xlabel)
            plt.legend(loc="best")
            plt.grid()
            key = key.replace(" ", "_")
            fig.savefig(
                f"./{self.out_dir}/Model_vs_{metamod_name}Model_{key}.{self.out_format}",
                bbox_inches="tight",
            )
            plt.close()
