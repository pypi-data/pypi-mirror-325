# -*- coding: utf-8 -*-
"""
Test the PCE class in bayesvalidrox.
Class PCE: 
    build_metamodel  - x
    update_metamodel
    update_pce_coeffs
    create_basis_indices --removed, just redirects
    add_input_space                                   -x
    univ_basis_vals
    fit
    adaptive_regression
    pca_transformation
    eval_metamodel
    create_model_error
    eval_model_error
    AutoVivification
    copy_meta_model_opts
    __select_degree
    generate_polynomials
    calculate_moments
    
"""
import numpy as np
import pytest
import sys

sys.path.append("../src/")

from bayesvalidrox.surrogate_models.inputs import Input
from bayesvalidrox.surrogate_models.input_space import InputSpace
from bayesvalidrox.surrogate_models.meta_model import MetaModel
from bayesvalidrox.surrogate_models.polynomial_chaos import PCE
from bayesvalidrox.surrogate_models.supplementary import corr_loocv_error, create_psi


@pytest.fixture
def PCE_1DwithInputSpace():
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    samples = np.array([[0.2], [0.8]])
    mm = PCE(inp)
    mm.CollocationPoints = samples
    mm.input_space = InputSpace(mm.input_obj, mm.meta_model_type)
    n_init_samples = samples.shape[0]
    mm.input_space.n_init_samples = n_init_samples
    mm.input_space.init_param_space(np.max(mm.pce_deg))
    return mm


#%% Test MetaMod constructor on its own

def test_metamod() -> None:
    """
    Construct PCE without inputs
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    PCE(inp)


#%% Test PCE.build_metamodel

#def test_build_metamodel_nosamples() -> None:
#    """
#    Build PCE without collocation samples
#    """
#    inp = Input()
#    inp.add_marginals()
#    inp.marginals[0].dist_type = 'normal'
#    inp.marginals[0].parameters = [0, 1]
#    mm = PCE(inp)
#    with pytest.raises(AttributeError) as excinfo:
#        mm.build_metamodel()
#    assert str(excinfo.value) == 'Please provide samples to the metamodel before building it.'


def test_build_metamodel(PCE_1DwithInputSpace) -> None:
    """
    Build PCE
    """
    mm = PCE_1DwithInputSpace
    mm.CollocationPoints = np.array([[0.2], [0.8]])
    mm.build_metamodel()


#%% Test PCE._generate_polynomials

def test__generate_polynomials_noexp() -> None:
    """
    Generate polynomials without ExpDeg
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)
    with pytest.raises(AttributeError) as excinfo:
        mm._generate_polynomials()
    assert str(excinfo.value) == 'Generate or add InputSpace before generating polynomials'


def test__generate_polynomials_nodeg() -> None:
    """
    Generate polynomials without max_deg
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)

    # Setup
    mm.input_space = InputSpace(inp)
    mm.input_space.n_init_samples = 2
    mm.input_space.init_param_space(np.max(mm.pce_deg))
    mm.ndim = mm.input_space.ndim
    mm.n_params = len(mm.input_obj.marginals)

    # Generate
    with pytest.raises(AttributeError) as excinfo:
        mm._generate_polynomials()
    assert str(excinfo.value) == 'MetaModel cannot generate polynomials in the given scenario!'


def test__generate_polynomials_deg() -> None:
    """
    Generate polynomials with max_deg
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)

    # Setup
    mm.input_space = InputSpace(inp)
    mm.input_space.n_init_samples = 2
    mm.input_space.init_param_space(np.max(mm.pce_deg))
    mm.ndim = mm.input_space.ndim
    mm.n_params = len(mm.input_obj.marginals)

    # Generate
    mm._generate_polynomials(4)


#%% Test MetaMod.add_input_space

def test_add_input_space() -> None:
    """
    Add InputSpace in PCE
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)
    mm.add_input_space()


#%% Test PCE.fit
# Faster without these
def test_fit() -> None:
    """
    Fit PCE
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)
    mm.fit([[0.2], [0.4], [0.8]], {'Z': [[0.4], [0.2], [0.5]]})


# def test_fit_parallel() -> None:
#     """
#     Fit PCE in parallel
#     """
#     inp = Input()
#     inp.add_marginals()
#     inp.marginals[0].dist_type = 'normal'
#     inp.marginals[0].parameters = [0, 1]
#     mm = PCE(inp)
#     mm.fit([[0.2], [0.4], [0.8]], {'Z': [[0.4], [0.2], [0.5]]}, parallel=True)


# def test_fit_verbose() -> None:
#     """
#     Fit PCE verbose
#     """
#     inp = Input()
#     inp.add_marginals()
#     inp.marginals[0].dist_type = 'normal'
#     inp.marginals[0].parameters = [0, 1]
#     mm = PCE(inp)
#     mm.fit([[0.2], [0.4], [0.8]], {'Z': [[0.4], [0.2], [0.5]]}, verbose=True)


def test_fit_pca() -> None:
    """
    Fit PCE verbose and with pca
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)
    mm.dim_red_method = 'pca'
    mm.fit([[0.2], [0.4], [0.8]], {'Z': [[0.4], [0.2], [0.5]]}, verbose=True)



#%% Test PCE.regression

def test_regression(PCE_1DwithInputSpace) -> None:
    """
    Regression without a method
    """
    mm = PCE_1DwithInputSpace
    samples = np.array([[0.2]])
    outputs = np.array([0.5])

    mm.CollocationPoints = samples
    mm.build_metamodel()
    BasisIndices = mm._all_basis_indices[str(1)][str(1.0)]
    univ_bas = mm.univ_basis_vals(samples)
    psi = create_psi(BasisIndices, univ_bas)

    mm.regression(samples, outputs, psi)


def test_regression_ols(PCE_1DwithInputSpace) -> None:
    """
    Regression: ols
    """
    mm = PCE_1DwithInputSpace
    samples = np.array([[0.2]])
    outputs = np.array([0.5])

    mm.CollocationPoints = samples
    mm.build_metamodel()
    BasisIndices = mm._all_basis_indices[str(1)][str(1.0)]
    univ_bas = mm.univ_basis_vals(samples)
    psi = create_psi(BasisIndices, univ_bas)

    mm._pce_reg_method = 'ols'
    mm.regression(samples, outputs, psi)


def test_regression_olssparse(PCE_1DwithInputSpace) -> None:
    """
    Regression: ols and sparse
    """
    mm = PCE_1DwithInputSpace
    samples = np.array([[0.2]])
    outputs = np.array([0.5])

    mm.CollocationPoints = samples
    mm.build_metamodel()
    BasisIndices = mm._all_basis_indices[str(1)][str(1.0)]
    univ_bas = mm.univ_basis_vals(samples)
    psi = create_psi(BasisIndices, univ_bas)

    mm._pce_reg_method = 'ols'
    mm.regression(samples, outputs, psi, sparsity=True)


def test_regression_ard(PCE_1DwithInputSpace) -> None:
    """
    Regression: ard
    """
    mm = PCE_1DwithInputSpace
    samples = np.array([[0.2], [0.8]])
    outputs = np.array([0.4, 0.5])

    mm.CollocationPoints = samples
    mm.build_metamodel()
    BasisIndices = mm._all_basis_indices[str(1)][str(1.0)]
    univ_bas = mm.univ_basis_vals(samples)
    psi = create_psi(BasisIndices, univ_bas)

    mm._pce_reg_method = 'ard'
    mm.regression(samples, outputs, psi)


def test_regression_ardssparse(PCE_1DwithInputSpace) -> None:
    """
    Regression: ard and sparse
    """
    mm = PCE_1DwithInputSpace
    samples = np.array([[0.2], [0.8]])
    outputs = np.array([0.4, 0.5])

    mm.CollocationPoints = samples
    mm.build_metamodel()
    BasisIndices = mm._all_basis_indices[str(1)][str(1.0)]
    univ_bas = mm.univ_basis_vals(samples)
    psi = create_psi(BasisIndices, univ_bas)

    mm._pce_reg_method = 'ard'
    mm.regression(samples, outputs, psi, sparsity=True)


def test_regression_fastard(PCE_1DwithInputSpace) -> None:
    """
    Regression: fastard
    """
    mm = PCE_1DwithInputSpace
    samples = np.array([[0.2]])
    outputs = np.array([0.5])

    mm.CollocationPoints = samples
    mm.build_metamodel()
    BasisIndices = mm._all_basis_indices[str(1)][str(1.0)]
    univ_bas = mm.univ_basis_vals(samples)
    psi = create_psi(BasisIndices, univ_bas)

    mm._pce_reg_method = 'fastard'
    mm.regression(samples, outputs, psi)


def test_regression_fastardssparse(PCE_1DwithInputSpace) -> None:
    """
    Regression: fastard and sparse
    """
    mm = PCE_1DwithInputSpace
    samples = np.array([[0.2]])
    outputs = np.array([0.5])

    mm.CollocationPoints = samples
    mm.build_metamodel()
    BasisIndices = mm._all_basis_indices[str(1)][str(1.0)]
    univ_bas = mm.univ_basis_vals(samples)
    psi = create_psi(BasisIndices, univ_bas)

    mm._pce_reg_method = 'fastard'
    mm.regression(samples, outputs, psi, sparsity=True)


def test_regression_brr(PCE_1DwithInputSpace) -> None:
    """
    Regression: brr
    """
    mm = PCE_1DwithInputSpace
    samples = np.array([[0.2]])
    outputs = np.array([0.5])

    mm.CollocationPoints = samples
    mm.build_metamodel()
    BasisIndices = mm._all_basis_indices[str(1)][str(1.0)]
    univ_bas = mm.univ_basis_vals(samples)
    psi = create_psi(BasisIndices, univ_bas)

    mm._pce_reg_method = 'brr'
    mm.regression(samples, outputs, psi)


def test_regression_brrssparse(PCE_1DwithInputSpace) -> None:
    """
    Regression: brr and sparse
    """
    mm = PCE_1DwithInputSpace
    samples = np.array([[0.2]])
    outputs = np.array([0.5])

    mm.CollocationPoints = samples
    mm.build_metamodel()
    BasisIndices = mm._all_basis_indices[str(1)][str(1.0)]
    univ_bas = mm.univ_basis_vals(samples)
    psi = create_psi(BasisIndices, univ_bas)

    mm._pce_reg_method = 'brr'
    mm.regression(samples, outputs, psi, sparsity=True)


if 0: # Could not figure out these errors, issue most likely in chosen samples/outputs
    def test_regression_bcs(PCE_1DwithInputSpace) -> None:
        """
        Regression: bcs
        """
        mm = PCE_1DwithInputSpace
        samples = np.array([[0.0], [0.1], [0.2], [0.3], [0.4], [0.5], [0.6], [0.7], [0.8], [0.9]])
        outputs = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
        mm.pce_deg = 3
        mm.CollocationPoints = samples
        mm.build_metamodel()
        BasisIndices = mm._all_basis_indices[str(mm.pce_deg)][str(1.0)]
        univ_bas = mm.univ_basis_vals(samples)
        psi = create_psi(BasisIndices, univ_bas)
    
        mm._pce_reg_method = 'bcs'
        mm.regression(samples, outputs, psi)
    
    
    def test_regression_bcsssparse(PCE_1DwithInputSpace) -> None:
        """
        Regression: bcs and sparse
        """
        mm = PCE_1DwithInputSpace
        samples = np.array([[0.0], [0.1], [0.2], [0.3], [0.4], [0.5], [0.6], [0.7], [0.8], [0.9], [1.0]])
        outputs = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.1])
    
        mm.CollocationPoints = samples
        mm.build_metamodel()
        BasisIndices = mm._all_basis_indices[str(1)][str(1.0)]
        univ_bas = mm.univ_basis_vals(samples)
        psi = create_psi(BasisIndices, univ_bas)
    
        mm._pce_reg_method = 'bcs'
        mm.regression(samples, outputs, psi, sparsity=True)


def test_regression_lars(PCE_1DwithInputSpace) -> None:
    """
    Regression: lars
    """
    mm = PCE_1DwithInputSpace
    samples = np.array([[0.0], [0.1], [0.2], [0.3], [0.4], [0.5], [0.6], [0.7], [0.8], [0.9], [1.0]])
    outputs = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.1])

    mm.CollocationPoints = samples
    mm.build_metamodel()
    BasisIndices = mm._all_basis_indices[str(1)][str(1.0)]
    univ_bas = mm.univ_basis_vals(samples)
    psi = create_psi(BasisIndices, univ_bas)

    mm._pce_reg_method = 'lars'
    mm.regression(samples, outputs, psi)


def test_regression_larsssparse(PCE_1DwithInputSpace) -> None:
    """
    Regression: lars and sparse
    """
    mm = PCE_1DwithInputSpace
    samples = np.array([[0.0], [0.1], [0.2], [0.3], [0.4], [0.5], [0.6], [0.7], [0.8], [0.9], [1.0]])
    outputs = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.1])

    mm.CollocationPoints = samples
    mm.build_metamodel()
    BasisIndices = mm._all_basis_indices[str(1)][str(1.0)]
    univ_bas = mm.univ_basis_vals(samples)
    psi = create_psi(BasisIndices, univ_bas)

    mm._pce_reg_method = 'lars'
    mm.regression(samples, outputs, psi, sparsity=True)


def test_regression_sgdr(PCE_1DwithInputSpace) -> None:
    """
    Regression: sgdr
    """
    mm = PCE_1DwithInputSpace
    samples = np.array([[0.2]])
    outputs = np.array([0.5])

    mm.CollocationPoints = samples
    mm.build_metamodel()
    BasisIndices = mm._all_basis_indices[str(1)][str(1.0)]
    univ_bas = mm.univ_basis_vals(samples)
    psi = create_psi(BasisIndices, univ_bas)

    mm._pce_reg_method = 'sgdr'
    mm.regression(samples, outputs, psi)


def test_regression_sgdrssparse(PCE_1DwithInputSpace) -> None:
    """
    Regression: sgdr and sparse
    """
    mm = PCE_1DwithInputSpace
    samples = np.array([[0.2]])
    outputs = np.array([0.5])

    mm.CollocationPoints = samples
    mm.build_metamodel()
    BasisIndices = mm._all_basis_indices[str(1)][str(1.0)]
    univ_bas = mm.univ_basis_vals(samples)
    psi = create_psi(BasisIndices, univ_bas)

    mm._pce_reg_method = 'sgdr'
    mm.regression(samples, outputs, psi, sparsity=True)


if 0: # Could not figure out these errors, issue most likely in chosen samples/outputs
    def test_regression_omp(PCE_1DwithInputSpace) -> None:
        """
        Regression: omp
        """
        mm = PCE_1DwithInputSpace
        samples = np.array([[0.0], [0.1], [0.2], [0.3], [0.4], [0.5], [0.6], [0.7], [0.8], [0.9], [1.0]])
        outputs = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1])
    
        mm.CollocationPoints = samples
        mm.build_metamodel()
        BasisIndices = mm._all_basis_indices[str(1)][str(1.0)]
        univ_bas = mm.univ_basis_vals(samples)
        psi = create_psi(BasisIndices, univ_bas)
    
        mm.regression(samples, outputs, psi, reg_method='omp')
    
    
    def test_regression_ompssparse(PCE_1DwithInputSpace) -> None:
        """
        Regression: omp and sparse
        """
        mm = PCE_1DwithInputSpace
        samples = np.array([[0.2]])
        outputs = np.array([0.5])
    
        mm.CollocationPoints = samples
        mm.build_metamodel()
        BasisIndices = mm._all_basis_indices[str(1)][str(1.0)]
        univ_bas = mm.univ_basis_vals(samples)
        psi = create_psi(BasisIndices, univ_bas)
    
        mm.regression(samples, outputs, psi, reg_method='omp', sparsity=True)


def test_regression_vbl(PCE_1DwithInputSpace) -> None:
    """
    Regression: vbl
    """
    mm = PCE_1DwithInputSpace
    samples = np.array([[0.2]])
    outputs = np.array([0.5])

    mm.CollocationPoints = samples
    mm.build_metamodel()
    BasisIndices = mm._all_basis_indices[str(1)][str(1.0)]
    univ_bas = mm.univ_basis_vals(samples)
    psi = create_psi(BasisIndices, univ_bas)

    mm._pce_reg_method = 'vbl'
    mm.regression(samples, outputs, psi)


def test_regression_vblssparse(PCE_1DwithInputSpace) -> None:
    """
    Regression: vbl and sparse
    """
    mm = PCE_1DwithInputSpace
    samples = np.array([[0.2]])
    outputs = np.array([0.5])

    mm.CollocationPoints = samples
    mm.build_metamodel()
    BasisIndices = mm._all_basis_indices[str(1)][str(1.0)]
    univ_bas = mm.univ_basis_vals(samples)
    psi = create_psi(BasisIndices, univ_bas)

    mm._pce_reg_method = 'vbl'
    mm.regression(samples, outputs, psi, sparsity=True)


def test_regression_ebl(PCE_1DwithInputSpace) -> None:
    """
    Regression: ebl
    """
    mm = PCE_1DwithInputSpace
    samples = np.array([[0.2]])
    outputs = np.array([0.5])

    mm.CollocationPoints = samples
    mm.build_metamodel()
    BasisIndices = mm._all_basis_indices[str(1)][str(1.0)]
    univ_bas = mm.univ_basis_vals(samples)
    psi = create_psi(BasisIndices, univ_bas)

    mm._pce_reg_method = 'ebl'
    mm.regression(samples, outputs, psi)


def test_regression_eblssparse(PCE_1DwithInputSpace) -> None:
    """
    Regression: ebl and sparse
    """
    mm = PCE_1DwithInputSpace
    samples = np.array([[0.2]])
    outputs = np.array([0.5])

    mm.CollocationPoints = samples
    mm.build_metamodel()
    BasisIndices = mm._all_basis_indices[str(1)][str(1.0)]
    univ_bas = mm.univ_basis_vals(samples)
    psi = create_psi(BasisIndices, univ_bas)

    mm._pce_reg_method = 'ebl'
    mm.regression(samples, outputs, psi, sparsity=True)


#%% Test Model.update_pce_coeffs

# TODO: very linked to the actual training...

#%% Test PCE.univ_basis_vals

def test_univ_basis_vals(PCE_1DwithInputSpace) -> None:
    """
    Creates univariate polynomials
    """
    mm = PCE_1DwithInputSpace
    samples = np.array([[0.2], [0.8]])
    mm.CollocationPoints = samples
    mm.build_metamodel()
    mm.univ_basis_vals(samples)


#%% Test PCE.adaptive_regression

#def test_adaptive_regression_fewsamples(PCE_1DwithInputSpace) -> None:
#    """
#    Adaptive regression, no specific method, too few samples given
#    """
#    mm = PCE_1DwithInputSpace
#    samples = np.array([[0.2]])
#    outputs = np.array([0.8])
#    mm.CollocationPoints = samples
#    mm.build_metamodel()

#    # Evaluate the univariate polynomials on InputSpace
#    mm.univ_p_val = mm.univ_basis_vals(mm.CollocationPoints)
#    with pytest.raises(AttributeError) as excinfo:
#        mm.adaptive_regression(samples, outputs, 0)
#    assert str(excinfo.value) == ('There are too few samples for the corrected loo-cv error. Fit surrogate on at least as '
#                           'many samples as parameters to use this')



def test_adaptive_regression(PCE_1DwithInputSpace) -> None:
    """
    Adaptive regression, no specific method
    """
    mm = PCE_1DwithInputSpace
    samples = np.array([[0.0], [0.1]])
    outputs = np.array([0.0, 0.1])

    mm.CollocationPoints = samples
    mm.build_metamodel()

    # Evaluate the univariate polynomials on InputSpace
    mm.univ_p_val = mm.univ_basis_vals(mm.CollocationPoints)
    mm.adaptive_regression(samples, outputs, 0)


def test_adaptive_regression_verbose(PCE_1DwithInputSpace) -> None:
    """
    Adaptive regression, no specific method, verbose output
    """
    mm = PCE_1DwithInputSpace
    samples = np.array([[0.0], [0.1]])
    outputs = np.array([0.0, 0.1])

    mm.CollocationPoints = samples
    mm.build_metamodel()

    # Evaluate the univariate polynomials on InputSpace
    mm.univ_p_val = mm.univ_basis_vals(mm.CollocationPoints)
    mm.adaptive_regression(samples, outputs, 0, True)


def test_adaptive_regression_ols(PCE_1DwithInputSpace) -> None:
    """
    Adaptive regression, ols
    """
    mm = PCE_1DwithInputSpace
    samples = np.array([[0.0], [0.1], [0.2], [0.3], [0.4], [0.5], [0.6], [0.7], [0.8],
                        [0.9], [1.0]])
    outputs = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.1])

    mm.CollocationPoints = samples
    mm.build_metamodel()

    # Evaluate the univariate polynomials on InputSpace
    mm.univ_p_val = mm.univ_basis_vals(mm.CollocationPoints)
    mm._pce_reg_method = 'ols'
    mm.adaptive_regression(samples, outputs, 0)


#%% Test PCE.pca_transformation

def test_pca_transformation() -> None:
    """
    Apply PCA
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)
    outputs = np.array([[0.4, 0.4], [0.5, 0.6]])
    mm.pca_transformation(outputs, 1)


def test_pca_transformation_varcomp() -> None:
    """
    Apply PCA with set var_pca_threshold
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)
    outputs = np.array([[0.4, 0.4], [0.5, 0.6]])
    mm.var_pca_threshold = 1
    mm.pca_transformation(outputs, 1)



#%% Test PCE.eval_metamodel

def test_eval_metamodel() -> None:
    """
    Eval trained PCE 
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)
    mm.out_names = ['Z']
    mm.fit([[0.2], [0.4], [0.8]], {'Z': [[0.4], [0.2], [0.5]]})
    mm.eval_metamodel([[0.4]])


def test_eval_metamodel_normalboots() -> None:
    """
    Eval trained PCE with normal bootstrap
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)
    mm.bootstrap_method = 'normal'
    mm.out_names = ['Z']
    mm.fit([[0.2], [0.4], [0.8]], {'Z': [[0.4], [0.2], [0.5]]})
    mm.eval_metamodel([[0.4]])


def test_eval_metamodel_highnormalboots() -> None:
    """
    Eval trained PCE with higher bootstrap-itrs
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)
    mm.n_bootstrap_itrs = 2
    mm.out_names = ['Z']
    mm.fit([[0.2], [0.4], [0.8]], {'Z': [[0.4], [0.2], [0.5]]})
    mm.eval_metamodel([[0.4]])


def test_eval_metamodel_pca() -> None:
    """
    Eval trained PCE with pca
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)
    mm.dim_red_method = 'pca'
    mm.out_names = ['Z']
    mm.fit([[0.2], [0.8]], {'Z': [[0.4, 0.4], [0.5, 0.6]]})
    mm.eval_metamodel([[0.4]])


#%% Test PCE.create_model_error
# TODO: move model out of this function

#%% Test PCE.eval_model_error
# TODO: test create_model_error first

#%% Test PCE.AutoVivification
def test_AutoVivification() -> None:
    """
    Creation of auto-vivification objects
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)
    mm.AutoVivification()


#%% Test PCE.copy_meta_model_opts

def test_copy_meta_model_opts() -> None:
    """
    Copy the PCE with just some stats
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)
    mm.add_input_space()
    mm.copy_meta_model_opts()


#%% Test PCE.__select_degree

#%% Test PCE.calculate_moments

def test_calculate_moments() -> None:
    """
    Calculate moments of a pce-surrogate
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)
    mm.fit([[0.2], [0.4], [0.8]], {'Z': [[0.4], [0.2], [0.5]]})
    mm.calculate_moments()


def test_calculate_moments_pca() -> None:
    """
    Calculate moments of a pce-surrogate with pca
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)
    mm.dim_red_method = 'pca'
    mm.fit([[0.2], [0.8]], {'Z': [[0.4, 0.4], [0.5, 0.6]]})
    mm.calculate_moments()


def test_calculate_moments_verbose() -> None:
    """
    Calculate moments of a pce-surrogate with pca
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)
    mm.verbose = True
    mm.fit([[0.2], [0.8]], {'Z': [[0.4, 0.4], [0.5, 0.6]]})
    mm.calculate_moments()


#%% Test PCE.update_metamodel
# TODO: taken from engine


#%% Test PCE.calculate_sobol

def test_calculate_sobol():
    """
    Calculate Sobol' indices of a pce-surrogate
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)
    mm.fit([[0.2], [0.8]], {'Z': [[0.4, 0.4], [0.5, 0.6]]})
    sobol, totalsobol = mm.calculate_sobol()
    # TODO are there theory-related checks that could be applied here?

    
def test_calculate_sobol_pca():
    """
    Calculate Sobol' indices of a pce-surrogate with PCA
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)
    mm.dim_red_method = 'pca'
    mm.fit([[0.2], [0.8]], {'Z': [[0.4, 0.4], [0.5, 0.6]]})
    sobol, totalsobol = mm.calculate_sobol({'Z': np.array([[0.4, 0.4], [0.5, 0.6]])})
    # TODO are there theory-related checks that could be applied here?

def test_calculate_sobol_pcanoy():
    """
    Calculate Sobol' indices of a pce-surrogate with PCA but no outputs
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)
    mm.dim_red_method = 'pca'
    mm.fit([[0.2], [0.8]], {'Z': [[0.4, 0.4], [0.5, 0.6]]})

    with pytest.raises(AttributeError) as excinfo:
        mm.calculate_sobol()
    assert str(excinfo.value) == ("Calculation of Sobol' indices with PCA expects training outputs, but none are given.")

