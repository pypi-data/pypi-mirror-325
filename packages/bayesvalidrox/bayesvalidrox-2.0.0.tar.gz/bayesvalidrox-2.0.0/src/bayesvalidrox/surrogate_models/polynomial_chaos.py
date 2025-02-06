#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementation of metamodel as PC or aPC
"""

import copy
import os
import warnings

import functools
import math
from itertools import combinations
import matplotlib.pyplot as plt
import numpy as np
import sklearn.linear_model as lm
from joblib import Parallel, delayed
from tqdm import tqdm

from .apoly_construction import apoly_construction
from .bayes_linear import VBLinearRegression, EBLinearRegression
from .eval_rec_rule import eval_univ_basis
from .glexindex import glexindex
from .orthogonal_matching_pursuit import OrthogonalMatchingPursuit
from .reg_fast_ard import RegressionFastARD
from .reg_fast_laplace import RegressionFastLaplace

from .meta_model import (
    MetaModel,
    _preprocessing_fit,
    _bootstrap_fit,
    _preprocessing_eval,
    _bootstrap_eval,
)

from .supplementary import corr_loocv_error, create_psi

warnings.filterwarnings("ignore")
# Load the mplstyle
# noinspection SpellCheckingInspection
plt.style.use(os.path.join(os.path.split(__file__)[0], "../", "bayesvalidrox.mplstyle"))


class PCE(MetaModel):
    """
    PCE MetaModel

    This class trains a surrogate model of type Polynomial Chaos Expansion.
    It accepts an input object (input_obj)
    containing the specification of the distributions for uncertain parameters
    and a model object with instructions on how to run the computational model.

    Attributes
    ----------
    input_obj : obj
        Input object with the information on the model input parameters.
    meta_model_type : str
        PCE-surrogate model types. Two surrogate model types are supported:
        polynomial chaos expansion (`PCE`), arbitrary PCE (`aPCE`).
        Default is PCE.
    pce_reg_method : str
        PCE regression method to compute the coefficients. The following
        regression methods are available:
        1. OLS: Ordinary Least Square method
        2. BRR: Bayesian Ridge Regression
        3. LARS: Least angle regression
        4. ARD: Bayesian ARD Regression
        5. FastARD: Fast Bayesian ARD Regression
        6. VBL: Variational Bayesian Learning
        7. EBL: Emperical Bayesian Learning
        Default is `OLS`.
    bootstrap_method : str
        Bootstraping method. Options are `'normal'` and `'fast'`. The default
        is `'fast'`. It means that in each iteration except the first one, only
        the coefficent are recalculated with the ordinary least square method.
    n_bootstrap_itrs : int
        Number of iterations for the bootstrap sampling. The default is `1`.
    pce_deg : int or list of int
        Polynomial degree(s). If a list is given, an adaptive algorithm is used
        to find the best degree with the lowest Leave-One-Out cross-validation
        (LOO) error (or the highest score=1-LOO). Default is `1`.
    pce_q_norm : float
        Hyperbolic (or q-norm) truncation for multi-indices of multivariate
        polynomials. Default is `1.0`.
    dim_red_method : str
        Dimensionality reduction method for the output space. The available
        method is based on principal component analysis (PCA). The Default is
        `'no'`. There are two ways to select number of components: use
        percentage of the explainable variance threshold (between 0 and 100)
        (Option A) or direct prescription of components' number (Option B):
            >>> MetaModelOpts = MetaModel()
            >>> MetaModelOpts.dim_red_method = 'PCA'
            >>> MetaModelOpts.var_pca_threshold = 99.999  # Option A
            >>> MetaModelOpts.n_pca_components = 12 # Option B
    verbose : bool
        Prints summary of the regression results. Default is `False`.
    """

    def __init__(
        self,
        input_obj,
        meta_model_type="PCE",
        pce_reg_method="OLS",
        bootstrap_method="fast",
        n_bootstrap_itrs=1,
        pce_deg=1,
        pce_q_norm=1.0,
        dim_red_method="no",
        verbose=False,
        input_transform="user",
    ):

        # Check if the surrogate outputs gaussian results
        self.pce_reg_method = pce_reg_method
        self.n_bootstrap_itrs = n_bootstrap_itrs
        is_gaussian = self.check_is_gaussian()

        # Use parent init
        super().__init__(
            input_obj,
            meta_model_type,
            bootstrap_method,
            n_bootstrap_itrs,
            dim_red_method,
            is_gaussian,
            verbose,
            input_transform,
        )

        # Additional inputs
        # Parameters that are not needed from the outside are denoted with '_'
        self.pce_deg = pce_deg
        self.pce_q_norm = pce_q_norm
        self.regression_dict = {}
        self._pce_reg_options = {}

        # These three parameters belong to the 'error_model'.
        #       Can this be removed to outside of this class?
        # self._errorScale = None
        # self._error_clf_poly = None
        # self._errorRegMethod = None

        # Other params
        self._polycoeffs = None
        self._univ_p_val = None
        self._all_basis_indices = None
        self._deg_array = None
        self.lc_error = None
        self._clf_poly = None
        self._basis_dict = None
        self._coeffs_dict = None
        self._q_norm_dict = None
        self._deg_dict = None

        self.sobol = None
        self.total_sobol = None

        # Initialize the regression options as a dictionary
        self.set_regression_options()

    def check_is_gaussian(self) -> bool:
        """
        Check if the metamodel returns a mean and stdev.

        Returns
        -------
        bool
            True if the metamodel can return estimations of uncertainty
            with each prediction. False otherwise.

        """
        if self.n_bootstrap_itrs > 1:
            return True
        if self.pce_reg_method.lower() == "ols":
            return False
        if self.pce_reg_method.lower() == "lars":
            return False
        return True

    def set_regression_options(self) -> None:
        """
        Collects the generic settings for the regression in a dictionary.
        This includes the regression objects and their arguments.

        Returns
        -------
        None

        """
        # Collect all regression objects
        self.regression_dict["ols"] = lm.LinearRegression
        self.regression_dict["brr"] = lm.BayesianRidge
        self.regression_dict["ard"] = lm.ARDRegression
        self.regression_dict["fastard"] = RegressionFastARD
        self.regression_dict["bcs"] = RegressionFastLaplace
        self.regression_dict["lars"] = lm.LassoLarsCV
        self.regression_dict["sgdr"] = lm.SGDRegressor
        self.regression_dict["omp"] = OrthogonalMatchingPursuit
        self.regression_dict["vbl"] = VBLinearRegression
        self.regression_dict["ebl"] = EBLinearRegression

        # Collect the corresponding options
        self._pce_reg_options["ols"] = {"fit_intercept": False}
        self._pce_reg_options["brr"] = {
            "n_iter": 1000,
            "tol": 1e-7,
            "fit_intercept": False,
            # 'compute_score':compute_score,
            "alpha_1": 1e-04,
            "alpha_2": 1e-04,
            # 'lambda_1':lambda_, 'lambda_2':lambda_
        }
        self._pce_reg_options["ard"] = {
            "fit_intercept": False,
            # 'compute_score':compute_score,
            "n_iter": 1000,
            "tol": 0.0001,
            "alpha_1": 1e-3,
            "alpha_2": 1e-3,
            # 'lambda_1':lambda_, 'lambda_2':lambda_
        }
        self._pce_reg_options["fastard"] = {
            "fit_intercept": False,
            "normalize": True,
            # 'compute_score':compute_score,
            "n_iter": 300,
            "tol": 1e-10,
        }
        self._pce_reg_options["bcs"] = {
            "fit_intercept": False,
            # 'bias_term':bias_term,
            "n_iter": 1000,
            "tol": 1e-7,
        }
        self._pce_reg_options["lars"] = {"fit_intercept": False}
        self._pce_reg_options["sgdr"] = {
            "fit_intercept": False,
            "max_iter": 5000,
            "tol": 1e-7,
        }
        self._pce_reg_options["omp"] = {"fit_intercept": False}
        self._pce_reg_options["vbl"] = {"fit_intercept": False}
        self._pce_reg_options["ebl"] = {"optimizer": "em"}

    def build_metamodel(self) -> None:
        """
        Builds the parts for the metamodel (polynomes,...) that are needed before fitting.
        This is executed outside of any loops related to e.g. bootstrap or
        transformations such as pca.

        Returns
        -------
        None

        """
        # Generate polynomials
        self._generate_polynomials(np.max(self.pce_deg))

        # Initialize the nested dictionaries
        self._deg_dict = self.AutoVivification()
        self._q_norm_dict = self.AutoVivification()
        self._coeffs_dict = self.AutoVivification()
        self._basis_dict = self.AutoVivification()
        self.loocv_score_dict = self.AutoVivification()
        self._clf_poly = self.AutoVivification()
        self.lc_error = self.AutoVivification()

        self._deg_array = self.__select_degree()  # self.ndim, self.n_samples)

        # Generate all basis indices
        self._all_basis_indices = self.AutoVivification()
        for deg in self._deg_array:
            keys = self._all_basis_indices.keys()
            if deg not in np.fromiter(keys, dtype=float):
                # Generate the polynomial basis indices
                for _, q in enumerate(self.pce_q_norm):
                    basis_indices = glexindex(
                        start=0,
                        stop=deg + 1,
                        dimensions=self.ndim,
                        cross_truncation=q,
                        reverse=False,
                        graded=True,
                    )
                    self._all_basis_indices[str(deg)][str(q)] = basis_indices

    @_preprocessing_fit
    @_bootstrap_fit
    def fit(self, X: np.array, y: dict, parallel=False, verbose=False, b_i=0):
        """
        Fits the surrogate to the given data (samples X, outputs y).
        Note here that the samples X should be the transformed samples provided
        by the experimental design if the transformation is used there.

        Parameters
        ----------
        X : 2D list or np.array of shape (#samples, #dim)
            The parameter value combinations that the model was evaluated at.
        y : dict of 2D lists or arrays of shape (#samples, #timesteps)
            The respective model evaluations.
        parallel : bool
            Set to True to run the training in parallel for various keys.
            The default is False.
        verbose : bool
            Set to True to obtain more information during runtime.
            The default is False.

        Returns
        -------
        None.

        """

        # For loop over the components/outputs
        if self.verbose and self.n_bootstrap_itrs == 1:
            items = tqdm(y.items(), desc="Fitting regression")
        else:
            items = y.items()
        for key, output in items:

            # Parallel fit regression
            out = None
            if parallel and (not self.bootstrap_method == "fast" or b_i == 0):
                out = Parallel(n_jobs=-1, backend="multiprocessing")(
                    delayed(self.adaptive_regression)(X, output[:, idx], idx)
                    for idx in range(output.shape[1])
                )
            elif not parallel and (not self.bootstrap_method == "fast" or b_i == 0):
                results = map(
                    functools.partial(self.adaptive_regression, X),
                    [output[:, idx] for idx in range(output.shape[1])],
                    range(output.shape[1]),
                )
                out = list(results)

            # Store the first out dictionary
            if self.bootstrap_method == "fast" and b_i == 0:
                self.first_out[key] = copy.deepcopy(out)

            # Update the coefficients with OLS during bootstrap-iters
            if b_i > 0 and self.bootstrap_method == "fast":
                out = self.update_pce_coeffs(X, output, self.first_out[key])

            # Create a dict to pass the variables
            for i in range(output.shape[1]):
                self._deg_dict[f"b_{b_i + 1}"][key][f"y_{i + 1}"] = out[i]["degree"]
                self._q_norm_dict[f"b_{b_i + 1}"][key][f"y_{i + 1}"] = out[i]["qnorm"]
                self._coeffs_dict[f"b_{b_i + 1}"][key][f"y_{i + 1}"] = out[i]["coeffs"]
                self._basis_dict[f"b_{b_i + 1}"][key][f"y_{i + 1}"] = out[i][
                    "multi_indices"
                ]
                self.loocv_score_dict[f"b_{b_i + 1}"][key][f"y_{i + 1}"] = out[i][
                    "loo_cv_score"
                ]
                self._clf_poly[f"b_{b_i + 1}"][key][f"y_{i + 1}"] = out[i]["clf_poly"]
                self.lc_error[f"b_{b_i+1}"][key][f"y_{i+1}"] = out[i]["lc_error"]

    # -------------------------------------------------------------------------

    def update_pce_coeffs(self, X, y, out_dict=None):
        """
        Updates the PCE coefficents using only the ordinary least square method
        for the fast version of the bootstrapping.

        Parameters
        ----------
        X : array of shape (n_samples, ndim)
            Training set. These samples should be already transformed.
        y : array of shape (n_samples, n_outs)
            The (transformed) model responses.
        out_dict : dict
            The training output dictionary of the first iteration, i.e.
            the surrogate model for the original experimental design.

        Returns
        -------
        final_out_dict : dict
            The updated training output dictionary.

        """
        # Make a copy
        final_out_dict = copy.deepcopy(out_dict)

        # Create the _univ_p_val based on the given X
        _univ_p_val = self.univ_basis_vals(X, n_max=np.max(self.pce_deg))

        # Loop over the points
        for i in range(y.shape[1]):

            # Extract nonzero basis indices
            nnz_idx = np.nonzero(out_dict[i]["coeffs"])[0]
            if len(nnz_idx) != 0:
                basis_indices = out_dict[i]["multi_indices"]

                # Evaluate the multivariate polynomials on X
                psi = create_psi(basis_indices, _univ_p_val)

                # Calulate the cofficients of surrogate model
                updated_out = self.regression(
                    psi, y[:, i], basis_indices, sparsity=False
                )

                # Update coeffs in out_dict
                final_out_dict[i]["coeffs"][nnz_idx] = updated_out["coeffs"]

        return final_out_dict

    # -------------------------------------------------------------------------

    def univ_basis_vals(self, samples, n_max=None):
        """
        Evaluates univariate regressors along input directions.

        Parameters
        ----------
        samples : array of shape (n_samples, ndim)
            Samples.
        n_max : int, optional
            Maximum polynomial degree. The default is `None`.

        Returns
        -------
        univ_basis: array of shape (n_samples, ndim, n_max+1)
            All univariate regressors up to n_max.
        """
        # Extract information
        poly_types = self.input_space.poly_types
        if samples.ndim != 2:
            samples = samples.reshape(1, len(samples))
        n_max = np.max(self.pce_deg) if n_max is None else n_max

        # Extract poly coeffs
        if self.input_space.input_data_given or self.meta_model_type.lower() == "apce":
            a_polycoeffs = self._polycoeffs
        else:
            a_polycoeffs = None

        # Evaluate univariate basis
        univ_basis = eval_univ_basis(samples, n_max, poly_types, a_polycoeffs)

        return univ_basis

    # -------------------------------------------------------------------------

    def regression(self, X, y, basis_indices, sparsity=True):
        """
        Fit regression using the regression method provided.

        Parameters
        ----------
        X : array of shape (n_samples, n_features)
            Training vector, where n_samples is the number of samples and
            n_features is the number of features.
        y : array of shape (n_samples,)
            Target values.
        basis_indices : array of shape (n_terms, ndim)
            Multi-indices of multivariate polynomials.
        reg_method : str, optional
            DESCRIPTION. The default is None.
        sparsity : bool
            Use with sparsity-inducing training methods. The default is True

        Returns
        -------
        return_out_dict : Dict
            Fitted estimator, spareMulti-Index, sparseX and coefficients.

        """
        # Bayes sparse adaptive aPCE
        _clf_poly = None
        reg_method = self.pce_reg_method.lower()
        kwargs = self._pce_reg_options[reg_method]

        # Add the last parameters
        if reg_method in ["brr", "ard", "fastard"]:
            compute_score = bool(self.verbose)
            kwargs["compute_score"] = compute_score

        if reg_method in ["brr", "ard"]:
            lambda_ = 1e-6
            if np.var(y) != 0:
                lambda_ = 1 / np.var(y)
            kwargs["lambda_1"] = lambda_
            kwargs["lambda_2"] = lambda_

        if reg_method == "bcs":
            bias_term = self.dim_red_method.lower() != "pca"
            kwargs["bias_term"] = bias_term

        # Handle any exceptions
        if reg_method == "ard":
            if X.shape[0] < 2:
                raise ValueError(
                    "Regression with ARD can only be performed for more than 2 samples"
                )
        if reg_method == "bcs":
            if X.shape[0] < 10:
                raise ValueError(
                    "Regression with BCS can only be performed for more than 10 samples"
                )
        if reg_method == "lars":
            if X.shape[0] < 10:
                raise ValueError(
                    "Regression with LARS can only be performed for more than 5 samples"
                )

        # Init the regression object
        _clf_poly = self.regression_dict[reg_method](**kwargs)

        # Apply any other settings
        if reg_method == "brr":
            _clf_poly.converged = True

        # Do the fit
        _clf_poly.fit(X, y)

        # Select the nonzero entries of coefficients
        if sparsity:
            nnz_idx = np.nonzero(_clf_poly.coef_)[0]
        else:
            nnz_idx = np.arange(_clf_poly.coef_.shape[0])

        # This is for the case where all outputs are zero, thereby
        # all coefficients are zero, or no nnz_idx were found
        if (y == 0).all() or len(nnz_idx) == 0:
            nnz_idx = np.insert(np.nonzero(_clf_poly.coef_)[0], 0, 0)

        # Get sparse basis indices and PSI matrix
        sparse_basis_indices = basis_indices[nnz_idx]
        sparse_x = X[:, nnz_idx]
        # Check if re-estimation of coefficients is necessary:
        if reg_method in ["lars"] and nnz_idx.shape[0] < _clf_poly.coef_.shape[0]:
            # Re-estimate PCE coefficients using OLS
            _clf_poly = lm.LinearRegression(fit_intercept=False)
            _clf_poly.fit(sparse_x, y)
            coeffs = _clf_poly.coef_
        else:
            # If no re-estimation is needed, extract the sparse coefficients from original solver
            coeffs = _clf_poly.coef_[nnz_idx]
            _clf_poly.coef_ = coeffs

        # Create a dict to pass the outputs
        return_out_dict = {}
        return_out_dict["clf_poly"] = _clf_poly
        return_out_dict["spareMulti-Index"] = sparse_basis_indices
        return_out_dict["sparePsi"] = sparse_x
        return_out_dict["coeffs"] = coeffs
        return return_out_dict

    # -------------------------------------------------------------------------

    def adaptive_regression(self, X, y, var_idx, verbose=False):
        """
        Adaptively fits the PCE model by comparing the scores of different
        degrees and q-norm.

        Parameters
        ----------
        X : array of shape (n_samples, ndim)
            Training set. These samples should be already transformed.
        y : array of shape (n_samples,)
            Target values, i.e. simulation results for the Experimental design.
        var_idx : int
            Index of the output.
        verbose : bool, optional
            Print out summary. The default is False.

        Returns
        -------
        return_vars : Dict
            Fitted estimator, best degree, best q-norm, loo_cv_score and
            coefficients.

        """

        # Initialization
        q_all_coeffs, all_coeffs = {}, {}
        q_all_indices_sparse, all_indices_sparse = {}, {}
        q_all_clf_poly, all_clf_poly = {}, {}
        q_all_in_terms, all_in_terms = {}, {}
        q_all_lc_error, all_lc_error = {}, {}

        # Evaluate the univariate polynomials
        _univ_p_val = self.univ_basis_vals(X)

        # Extract degree array and q-norm array
        _deg_array = np.array([*self._all_basis_indices], dtype=int)
        qnorm = [*self._all_basis_indices[str(int(_deg_array[0]))]]

        # Some options for EarlyStop
        error_increases = False
        # Stop degree, if LOO error does not decrease n_checks_degree times
        n_checks_degree = 3
        # Stop qNorm, if criterion isn't fulfilled n_checks_q_norm times
        n_checks_q_norm = 2
        n_qnorms = len(qnorm)
        q_norm_early_stop = True
        if n_qnorms < n_checks_q_norm + 1:
            q_norm_early_stop = False

        # =====================================================================
        # basis adaptive polynomial chaos: repeat the calculation by increasing
        # polynomial degree until the highest accuracy is reached
        # =====================================================================
        # For each degree check all q-norms and choose the best one
        best_q = None
        scores = -np.inf * np.ones(_deg_array.shape[0])
        q_norm_scores = -np.inf * np.ones(n_qnorms)

        for deg_idx, deg in enumerate(_deg_array):

            for qidx, q in enumerate(qnorm):

                # Extract the polynomial basis indices from the pool of
                # _all_basis_indices
                basis_indices = self._all_basis_indices[str(deg)][str(q)]

                # Assemble the Psi matrix
                psi = create_psi(basis_indices, _univ_p_val)

                # Calulate the cofficients of the metamodel
                outs = self.regression(psi, y, basis_indices)

                # Calculate and save the score of LOOCV
                score, lc_error = corr_loocv_error(
                    outs["clf_poly"], outs["sparePsi"], outs["coeffs"], y
                )

                # Check the convergence of noise for FastARD
                if (
                    self.pce_reg_method == "FastARD"
                    and outs["clf_poly"].alpha_ < np.finfo(np.float32).eps
                ):
                    score = -np.inf

                q_norm_scores[qidx] = score
                q_all_coeffs[str(qidx + 1)] = outs["coeffs"]
                q_all_indices_sparse[str(qidx + 1)] = outs["spareMulti-Index"]
                q_all_clf_poly[str(qidx + 1)] = outs["clf_poly"]
                q_all_in_terms[str(qidx + 1)] = basis_indices.shape[0]
                q_all_lc_error[str(qidx + 1)] = lc_error

                # EarlyStop check
                # if there are at least n_checks_q_norm entries after the
                # best one, we stop
                if (
                    q_norm_early_stop
                    and sum(np.isfinite(q_norm_scores)) > n_checks_q_norm
                ):
                    # If the error has increased the last two iterations, stop!
                    q_norm_scores_noninf = q_norm_scores[np.isfinite(q_norm_scores)]
                    deltas = np.sign(np.diff(q_norm_scores_noninf))
                    if sum(deltas[-n_checks_q_norm + 1 :]) == 2:
                        # stop the q-norm loop here
                        break
                if np.var(y) == 0:
                    break

            # Store the score in the scores list
            best_q = np.nanargmax(q_norm_scores)
            scores[deg_idx] = q_norm_scores[best_q]

            all_coeffs[str(deg_idx + 1)] = q_all_coeffs[str(best_q + 1)]
            all_indices_sparse[str(deg_idx + 1)] = q_all_indices_sparse[str(best_q + 1)]
            all_clf_poly[str(deg_idx + 1)] = q_all_clf_poly[str(best_q + 1)]
            all_in_terms[str(deg_idx + 1)] = q_all_in_terms[str(best_q + 1)]
            all_lc_error[str(deg_idx + 1)] = q_all_lc_error[str(best_q + 1)]

            # Check the direction of the error (on average):
            # if it increases consistently stop the iterations
            if len(scores[scores != -np.inf]) > n_checks_degree:
                scores_noninf = scores[scores != -np.inf]
                ss = np.sign(scores_noninf - np.max(scores_noninf))
                # ss<0 error decreasing
                error_increases = np.sum(np.sum(ss[-2:])) <= -1 * n_checks_degree

            if error_increases:
                break

            # Check only one degree, if target matrix has zero variance
            if np.var(y) == 0:
                break

        # ------------------ Summary of results ------------------
        # Select the one with the best score and save the necessary outputs
        best_deg = np.nanargmax(scores) + 1
        coeffs = all_coeffs[str(best_deg)]
        basis_indices = all_indices_sparse[str(best_deg)]
        _clf_poly = all_clf_poly[str(best_deg)]
        loo_cv_score = np.nanmax(scores)
        p = all_in_terms[str(best_deg)]
        lc_error = all_lc_error[str(best_deg)]
        degree = _deg_array[np.nanargmax(scores)]
        qnorm = float(qnorm[best_q])

        # ------------------ Print out Summary of results ------------------
        if self.verbose:
            # Create PSI_Sparse by removing redundent terms
            nnz_idx = np.nonzero(coeffs)[0]
            basis_indices_sparse = basis_indices[nnz_idx]

            print(f"Output variable {var_idx + 1}:")
            print(
                "The estimation of PCE coefficients converged at polynomial "
                f"degree {_deg_array[best_deg - 1]} with "
                f"{len(basis_indices_sparse)} terms (Sparsity index = "
                f"{round(len(basis_indices_sparse) / p, 3)})."
            )

            print(f"Final ModLOO error estimate: {1 - max(scores):.3e}")
            print("\n" + "-" * 50)

        if verbose:
            print("=" * 50)
            print(" " * 10 + " Summary of results ")
            print("=" * 50)

            print("Scores:\n", scores)
            print("Degree of best score:", self._deg_array[best_deg - 1])
            print("No. of terms:", len(basis_indices))
            print("Sparsity index:", round(len(basis_indices) / p, 3))
            print("Best Indices:\n", basis_indices)

            if self.pce_reg_method.lower() in ["brr", "ard"]:
                _, ax = plt.subplots(figsize=(12, 10))
                plt.title("Marginal log-likelihood")
                plt.plot(_clf_poly.scores_, color="navy", linewidth=2)
                plt.ylabel("Score")
                plt.xlabel("Iterations")
                if self.pce_reg_method.lower() == "bbr":
                    text = f"$\\alpha={_clf_poly.alpha_:.1f}$\n\
                        $\\lambda={_clf_poly.lambda_:.3f}$\n\
                        $L={_clf_poly.scores_[-1]:.1f}$"
                else:
                    text = f"$\\alpha={_clf_poly.alpha_:.1f}$\n$\
                        \\L={_clf_poly.scores_[-1]:.1f}$"

                plt.text(0.75, 0.5, text, fontsize=18, transform=ax.transAxes)
                plt.savefig(f"marg_loglik_{self.pce_reg_method}.png")
                plt.close()
            print("=" * 80)

        # Create a dict to pass the outputs
        return_vars = {}
        return_vars["clf_poly"] = _clf_poly
        return_vars["degree"] = degree
        return_vars["qnorm"] = qnorm
        return_vars["coeffs"] = coeffs
        return_vars["multi_indices"] = basis_indices
        return_vars["loo_cv_score"] = loo_cv_score
        return_vars["lc_error"] = lc_error

        return return_vars

    # -------------------------------------------------------------------------

    @_preprocessing_eval
    @_bootstrap_eval
    def eval_metamodel(self, samples, b_i=0):
        """
        Evaluates metamodel at the requested samples. One can also generate
        nsamples.

        Parameters
        ----------
        samples : array of shape (n_samples, ndim), optional
            Samples to evaluate metamodel at. The default is None.

        Returns
        -------
        mean_pred : dict
            Mean of the predictions.
        std_pred : dict
            Standard deviatioon of the predictions.
        """
        # Compute univariate bases for the given samples
        _univ_p_val = self.univ_basis_vals(samples, n_max=np.max(self.pce_deg))

        # Extract model dictionary
        model_dict = self._coeffs_dict[f"b_{b_i + 1}"]

        # Loop over outputs
        mean_pred = {}
        std_pred = {}
        for output, values in model_dict.items():
            mean = np.empty((len(samples), len(values)))
            std = np.empty((len(samples), len(values)))
            idx = 0
            for in_key, _ in values.items():

                # Assemble Psi matrix
                basis = self._basis_dict[f"b_{b_i + 1}"][output][in_key]
                psi = create_psi(basis, _univ_p_val)

                # Prediction
                if self.bootstrap_method != "fast" or b_i == 0:
                    # with error bar, i.e. use _clf_poly
                    _clf_poly = self._clf_poly[f"b_{b_i + 1}"][output][in_key]
                    try:
                        y_mean, y_std = _clf_poly.predict(psi, return_std=True)
                    except TypeError:
                        y_mean = _clf_poly.predict(psi)
                        y_std = np.zeros_like(y_mean)
                else:
                    # without error bar
                    coeffs = self._coeffs_dict[f"b_{b_i + 1}"][output][in_key]
                    y_mean = np.dot(psi, coeffs)
                    y_std = np.zeros_like(y_mean)

                mean[:, idx] = y_mean
                std[:, idx] = y_std
                idx += 1

            mean_pred[output] = mean
            std_pred[output] = std

        return mean_pred, std_pred

    # -------------------------------------------------------------------------
    def __select_degree(self):  # , ndim, n_samples):
        """
        Selects degree based on the number of samples and parameters in the
        sequential design.

        Parameters
        ----------
        ndim : int
            Dimension of the parameter space.
        n_samples : int
            Number of samples.

        Returns
        -------
        _deg_array: array
            The selected degrees.

        """
        # Define the _deg_array
        max_deg = np.max(self.pce_deg)
        min_deg = np.min(self.pce_deg)

        # The old options for sequential are commented out!!!
        # nitr = n_samples - self.input_space.n_init_samples

        # Check q-norm
        if not np.isscalar(self.pce_q_norm):
            self.pce_q_norm = np.array(self.pce_q_norm)
        else:
            self.pce_q_norm = np.array([self.pce_q_norm])

        # def M_uptoMax(maxDeg):
        #    n_combo = np.zeros(maxDeg)
        #    for i, d in enumerate(range(1, maxDeg + 1)):
        #        n_combo[i] = math.factorial(ndim + d)
        #        n_combo[i] /= math.factorial(ndim) * math.factorial(d)
        #    return n_combo

        deg_new = max_deg
        # d = nitr if nitr != 0 and self.ndim > 5 else 1
        # d = 1
        # min_index = np.argmin(abs(M_uptoMax(max_deg)-ndim*n_samples*d))
        # deg_new = range(1, max_deg+1)[min_index]

        if deg_new > min_deg and self.pce_reg_method.lower() != "fastard":
            _deg_array = np.arange(min_deg, deg_new + 1)
        else:
            _deg_array = np.array([deg_new])

        return _deg_array

    def _generate_polynomials(self, max_deg=None):
        """
        Generates (univariate) polynomials.

        Parameters
        ----------
        max_deg : int
            Maximum polynomial degree.

        Returns
        -------
        None
        """
        # Check for input_space
        if self.input_space is None:
            raise AttributeError(
                "Generate or add InputSpace before generating polynomials"
            )

        ndim = self.input_space.ndim
        # Create orthogonal polynomial coefficients if necessary
        if max_deg is not None:  # and self.input_obj.poly_coeffs_flag:
            self._polycoeffs = {}
            for par_idx in tqdm(
                range(ndim), ascii=True, desc="Computing orth. polynomial coeffs"
            ):
                poly_coeffs = apoly_construction(
                    self.input_space.raw_data[par_idx], max_deg
                )
                self._polycoeffs[f"p_{par_idx + 1}"] = poly_coeffs
        else:
            raise AttributeError(
                "MetaModel cannot generate polynomials in the given scenario!"
            )

    # -------------------------------------------------------------------------
    def calculate_moments(self):
        """
        Computes the first two moments using the PCE-based metamodel.

        Returns
        -------
        pce_means: dict
            The first moment (mean) of the surrogate.
        pce_stds: dict
            The second moment (standard deviation) of the surrogate.

        """
        outputs = self.out_names
        pce_means_b = {}
        pce_stds_b = {}

        for b_i in range(self.n_bootstrap_itrs):
            pce_means_b[b_i] = {}
            pce_stds_b[b_i] = {}
            _coeffs_dicts = self._coeffs_dict[f"b_{b_i + 1}"].items()

            for output, coef_dict in _coeffs_dicts:
                pce_mean = np.zeros((len(coef_dict)))
                pce_var = np.zeros((len(coef_dict)))

                for index, _ in coef_dict.items():
                    idx = int(index.split("_")[1]) - 1
                    coeffs = self._coeffs_dict[f"b_{b_i + 1}"][output][index]

                    if coeffs[0] != 0:
                        pce_mean[idx] = coeffs[0]
                    else:
                        _clf_poly = self._clf_poly[f"b_{b_i + 1}"][output]
                        pce_mean[idx] = _clf_poly[index].intercept_
                    pce_var[idx] = np.sum(np.square(coeffs[1:]))

                # Save predictions for each output
                if self.dim_red_method.lower() == "pca":
                    pca = self.pca[f"b_{b_i + 1}"][output]
                    pce_means_b[b_i][output] = pca.inverse_transform(pce_mean)
                    pce_stds_b[b_i][output] = pca.inverse_transform(np.sqrt(pce_var))
                else:
                    pce_means_b[b_i][output] = pce_mean
                    pce_stds_b[b_i][output] = np.sqrt(pce_var)

        # Change the order of nesting
        mean_all = {}
        for i in sorted(pce_means_b):
            for k, v in pce_means_b[i].items():
                if k not in mean_all:
                    mean_all[k] = [None] * len(pce_means_b)
                mean_all[k][i] = v
        std_all = {}
        for i in sorted(pce_stds_b):
            for k, v in pce_stds_b[i].items():
                if k not in std_all:
                    std_all[k] = [None] * len(pce_stds_b)
                std_all[k][i] = v

        # Back transformation if PCA is selected.
        pce_means, pce_stds = {}, {}
        for output in outputs:
            pce_means[output] = np.mean(mean_all[output], axis=0)
            pce_stds[output] = np.mean(std_all[output], axis=0)

        # Print a report table
        if self.verbose:
            for output in outputs:
                print(f"\n>>>>> Moments of {output} <<<<<")
                print("\nIndex  |  Mean   |  Std. deviation")
                print("-" * 35)
                print(
                    "\n".join(
                        f"{i+1}  |  {k:.3e}  |  {j:.3e}"
                        for i, (k, j) in enumerate(
                            zip(pce_means[output], pce_stds[output])
                        )
                    )
                )
            print("-" * 40)

        return pce_means, pce_stds

    def calculate_sobol(self, y_train=None):
        """
        Provides Sobol' indices as a sensitivity measure to infer the importance
        of the input parameters. See Eq. 27 in [1] for more details. For the
        case with Principal component analysis refer to [2].

        [1] Global sensitivity analysis: A flexible and efficient framework
        with an example from stochastic hydrogeology S. Oladyshkin, F.P.
        de Barros, W. Nowak  https://doi.org/10.1016/j.advwatres.2011.11.001

        [2] Nagel, J.B., Rieckermann, J. and Sudret, B., 2020. Principal
        component analysis and sparse polynomial chaos expansions for global
        sensitivity analysis and model calibration: Application to urban
        drainage simulation. Reliability Engineering & System Safety, 195,
        p.106737.

        Parameters
        ----------
        y_train: dict, optional
            Trainings outputs. They are needed when used in combination with PCA.
            The default is None

        Returns
        -------
        sobol : dict
            Sobol' indices of all available orders.
        totalsobol : dict
            Total Sobol' indices

        """
        if self.dim_red_method.lower() == "pca" and y_train is None:
            raise AttributeError(
                "Calculation of Sobol' indices with PCA expects training outputs,"
                + " but none are given."
            )

        max_order = np.max(self.pce_deg)
        n_params = len(self.input_obj.marginals)
        cov_zpq = np.zeros((n_params))
        outputs = self.out_names
        sobol_cell_b, total_sobol_b = {}, {}

        for b_i in range(self.n_bootstrap_itrs):
            sobol_cell_, total_sobol_ = {}, {}

            for output in outputs:
                n_meas_points = len(self._coeffs_dict[f"b_{b_i+1}"][output])

                # Initialize the (cell) array containing the (total) Sobol indices.
                sobol_array = dict.fromkeys(range(1, max_order + 1), [])
                sobol_cell_array = dict.fromkeys(range(1, max_order + 1), [])

                for i_order in range(1, max_order + 1):
                    n_comb = math.comb(n_params, i_order)
                    sobol_cell_array[i_order] = np.zeros((n_comb, n_meas_points))
                total_sobol_array = np.zeros((n_params, n_meas_points))

                # Initialize the cell to store the names of the variables
                total_variance = np.zeros((n_meas_points))
                for p_idx in range(n_meas_points):
                    basis = self._basis_dict[f"b_{b_i+1}"][output][f"y_{p_idx+1}"]
                    coeffs = self._coeffs_dict[f"b_{b_i+1}"][output][f"y_{p_idx+1}"]

                    # Compute total variance
                    total_variance[p_idx] = np.sum(np.square(coeffs[1:]))

                    nzidx = np.where(coeffs != 0)[0]
                    # Set all the Sobol indices equal to zero in the presence of a
                    # null output.
                    if len(nzidx) == 0:
                        for i_order in range(1, max_order + 1):
                            sobol_cell_array[i_order][:, p_idx] = 0

                    # Otherwise compute them from sums of the coefficients
                    else:
                        nz_basis = basis[nzidx]
                        for i_order in range(1, max_order + 1):
                            idx = np.where(np.sum(nz_basis > 0, axis=1) == i_order)
                            subbasis = nz_basis[idx]
                            z_ = np.array(list(combinations(range(n_params), i_order)))

                            for q in range(z_.shape[0]):
                                if total_variance[p_idx] == 0.0:
                                    sobol_cell_array[i_order][q, p_idx] = 0.0
                                else:
                                    subidx = np.prod(subbasis[:, z_[q]], axis=1) > 0
                                    sum_ind = nzidx[idx[0][subidx]]
                                    sobol = np.sum(np.square(coeffs[sum_ind]))
                                    sobol /= total_variance[p_idx]
                                    sobol_cell_array[i_order][q, p_idx] = sobol

                        # Compute the TOTAL Sobol indices.
                        for par_idx in range(n_params):
                            idx = nz_basis[:, par_idx] > 0
                            sum_ind = nzidx[idx]

                            if total_variance[p_idx] == 0.0:
                                total_sobol_array[par_idx, p_idx] = 0.0
                            else:
                                sobol = np.sum(np.square(coeffs[sum_ind]))
                                sobol /= total_variance[p_idx]
                                total_sobol_array[par_idx, p_idx] = sobol

                    # ----- if PCA selected: Compute covariance -----
                    if self.dim_red_method.lower() == "pca":
                        # Extract the basis indices (alpha) and coefficients for
                        # next component
                        if p_idx < n_meas_points - 1:
                            nextbasis = self._basis_dict[f"b_{b_i+1}"][output][
                                f"y_{p_idx+2}"
                            ]
                            if self.bootstrap_method != "fast" or b_i == 0:
                                clf_poly = self._clf_poly[f"b_{b_i+1}"][output][
                                    f"y_{p_idx+2}"
                                ]
                                next_coeffs = clf_poly.coef_
                            else:
                                next_coeffs = self._coeffs_dict[f"b_{b_i+1}"][output][
                                    f"y_{p_idx+2}"
                                ]

                            # Choose the common non-zero basis
                            mask = (basis[:, None] == nextbasis).all(-1).any(-1)
                            n_mask = (nextbasis[:, None] == basis).all(-1).any(-1)

                            # Compute the covariance in Eq 17.
                            for par_idx in range(n_params):
                                idx = (mask) & (basis[:, par_idx] > 0)
                                n_idx = (n_mask) & (nextbasis[:, par_idx] > 0)
                                try:
                                    cov_zpq[par_idx] += np.sum(
                                        np.dot(coeffs[idx], next_coeffs[n_idx])
                                    )
                                except:
                                    pass

                # Compute the sobol indices according to Ref. 2
                if self.dim_red_method.lower() == "pca":
                    n_c_points = y_train[output].shape[1]
                    pca = self.pca[f"b_{b_i+1}"][output]
                    comp_pca = pca.components_
                    n_comp = comp_pca.shape[0]
                    var_zp = pca.explained_variance_

                    # Extract the sobol index of the components
                    for i_order in range(1, max_order + 1):
                        n_comb = math.comb(n_params, i_order)
                        sobol_array[i_order] = np.zeros((n_comb, n_c_points))
                        z_ = np.array(list(combinations(range(n_params), i_order)))

                        # Loop over parameters
                        for q in range(z_.shape[0]):
                            s_zi = sobol_cell_array[i_order][q]

                            for t_idx in range(n_c_points):
                                var_yt = np.var(y_train[output][:, t_idx])
                                term1, term2 = 0.0, 0.0
                                if var_yt != 0.0:
                                    # Eq. 17
                                    for i in range(n_comp):
                                        a = s_zi[i] * var_zp[i]
                                        a *= comp_pca[i, t_idx] ** 2
                                        term1 += a

                                    # Term 2
                                    # term2 = 0.0
                                    # for i in range(nComp-1):
                                    #     term2 += cov_Z_p_q[q] * compPCA[i, tIdx]
                                    #     term2 *= compPCA[i+1, tIdx]
                                    # term2 *= 2

                                # Divide over total output variance Eq. 18
                                sobol_array[i_order][q, t_idx] = term1  # + term2
                                sobol_array[i_order][q, t_idx] /= var_yt

                    # Compute the TOTAL Sobol indices.
                    total_sobol = np.zeros((n_params, n_c_points))
                    for par_idx in range(n_params):
                        s_zi = total_sobol_array[par_idx]

                        for t_idx in range(n_c_points):
                            var_yt = np.var(y_train[output][:, t_idx])
                            term1, term2 = 0.0, 0.0
                            if var_yt != 0.0:
                                for i in range(n_comp):
                                    term1 += (
                                        s_zi[i] * var_zp[i] * (comp_pca[i, t_idx] ** 2)
                                    )
                                for i in range(n_comp - 1):
                                    term2 += (
                                        cov_zpq[par_idx]
                                        * comp_pca[i, t_idx]
                                        * comp_pca[i + 1, t_idx]
                                    )
                                term2 *= 2

                            total_sobol[par_idx, t_idx] = term1  # + term2

                            # Devide over total output variance Eq. 18
                            total_sobol[par_idx, t_idx] /= var_yt

                    sobol_cell_[output] = sobol_array
                    total_sobol_[output] = total_sobol
                else:
                    sobol_cell_[output] = sobol_cell_array
                    total_sobol_[output] = total_sobol_array

            # Save for each bootstrap iteration
            sobol_cell_b[b_i] = sobol_cell_
            total_sobol_b[b_i] = total_sobol_

        # Combine for Sobol' indices, one set of indices for each possible degree of interaction
        self.sobol = {}
        sobol_all = {}
        for i in sorted(sobol_cell_b):
            for k, v in sobol_cell_b[i].items():
                for l, _ in v.items():
                    if l not in sobol_all:
                        sobol_all[l] = {}
                    if k not in sobol_all[l]:
                        sobol_all[l][k] = [None] * len(sobol_cell_b)
                    sobol_all[l][k][i] = v[l]
        for i_order in range(1, max_order + 1):
            self.sobol[i_order] = {}
            for output in outputs:
                self.sobol[i_order][output] = np.mean(
                    [sobol_all[i_order][output]], axis=0
                )

        # Combine for Total Sobol' indices
        total_sobol_all = {}
        self.total_sobol = {}
        for i in sorted(total_sobol_b):
            for k, v in total_sobol_b[i].items():
                if k not in total_sobol_all:
                    total_sobol_all[k] = [None] * len(total_sobol_b)
                total_sobol_all[k][i] = v
        for output in outputs:
            self.total_sobol[output] = np.mean(total_sobol_all[output], axis=0)

        return self.sobol, self.total_sobol
