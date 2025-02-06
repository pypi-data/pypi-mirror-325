# -*- coding: utf-8 -*-
"""
Test the PostProcessing class in bayesvalidrox.
Tests are available for the following functions
Class PostProcessing: 
    init
    plot_moments
    valid_metamodel
    check_accuracy
    plot_seq_design_diagnostics
    sobol_indices
    plot_sobol 
    check_req_quality
    plot_metamodel_3d
    _plot_validation_multi
"""

import sys
sys.path.append("../src/")
import numpy as np
import pytest
import os 
import matplotlib

from bayesvalidrox.post_processing.post_processing import PostProcessing
from bayesvalidrox.surrogate_models.inputs import Input
from bayesvalidrox.surrogate_models.exp_designs import ExpDesigns
from bayesvalidrox.surrogate_models.meta_model import MetaModel
from bayesvalidrox.surrogate_models.polynomial_chaos import PCE
from bayesvalidrox.pylink.pylink import PyLinkForwardModel as PL
from bayesvalidrox.surrogate_models.engine import Engine
from bayesvalidrox import GPESkl

matplotlib.use("Agg")

@pytest.fixture
def basic_engine():
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = MetaModel(inp)
    mod = PL()
    expdes = ExpDesigns(inp)
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    engine.emulator = True
    
    return engine

@pytest.fixture
def engine_no_MetaModel():
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mod = PL()
    expdes = ExpDesigns(inp)
    engine = Engine(None, mod, expdes)
    engine.trained = True
    
    return engine

@pytest.fixture
def basic_engine_trained():
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]

    # Create and configure the MetaModel
    mm = MetaModel(inp)

    # Create the engine object
    engine = type('Engine', (object,), {})()
    engine.trained = True
    engine.meta_model = mm

    # Set up sequential design diagnostics data
    engine.SeqModifiedLOO = {'Z': np.array([0.1, 0.2, 0.3])}
    engine.seqValidError = {'Z': np.array([0.15, 0.25, 0.35])}
    engine.SeqKLD = {'Z': np.array([0.05, 0.1, 0.15])}
    engine.SeqBME = {'Z': np.array([0.02, 0.04, 0.06])}
    engine.seqRMSEMean = {'Z': np.array([0.12, 0.14, 0.16])}
    engine.seqRMSEStd = {'Z': np.array([0.03, 0.05, 0.07])}
    engine.SeqDistHellinger = {'Z': np.array([0.08, 0.09, 0.1])}

    # Configure experiment design
    expdes = ExpDesigns(inp)
    expdes.par_names = ["Parameter 1", "Parameter 2"]  # Names for the two input parameters
    expdes.x_values = {'X1': [0.1, 0.2, 0.3], 'X2': [0.4, 0.5, 0.6]}  # Mock parameter values per design step
    expdes.x = np.array([[0, 0], [1, 1], [0.5, 0.5], [0.1, 0.5]])  # Two input dimensions
    expdes.y = {'Z': [[0.4], [0.5], [0.3], [0.4]]}  # Output values
    engine.out_names = ['Z']
    engine.exp_design = expdes

    return engine

@pytest.fixture
def basic_engine_sequential():
    
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    
    mm = MetaModel(inp)
    mod = PL()
    
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 4
    expdes.n_max_samples = 4
    expdes.x = np.array([[0], [1], [0.5], [0.1]]) 
    expdes.y = {'Z': [[0.4], [0.5], [0.3], [0.4]]}  # Output values
    expdes.x_values = np.array([0])
    
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    engine.train = True
    engine.emulator = True
    
    engine.train_sequential()
    
    engine.SeqModifiedLOO = {'DKL_rep_1': np.array([[1.31565589e-10],
       [1.31413432e-10]])}
    engine.seqValidError = {}
    engine.SeqKLD = {'DKL_rep_1': np.array([[2.6296851 ],
       [2.60875351]])}
    engine.SeqBME = {'DKL_rep_1': np.array([[-19.33941695],
       [-19.29572507]])}
    engine.seqRMSEMean = {'DKL_rep_1': np.array([[1.02174823],
       [1.02174727]])}
    engine.seqRMSEStd = {'DKL_rep_1': np.array([[0.76724993],
       [0.76725023]])}
    engine.SeqDistHellinger = {}
    
    for key, array in engine.SeqModifiedLOO.items():
        assert np.all(array != None), f"Array {key} contains None values."
    
    return engine

@pytest.fixture
def pce_engine():
    inp = Input()
    
    inp.add_marginals()
    inp.marginals[0].name = 'x'
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    
    expdes = ExpDesigns(inp)
    expdes.init_param_space(max_deg=1)
    expdes.x = np.array([[0], [1], [0.5]])
    expdes.y = {'Z': [[0.4], [0.5], [0.45]]}
    expdes.x_values = [0]

    mm = PCE(inp)
    mm.fit(expdes.x, expdes.y)
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    engine.emulator = True
    engine.trained = True
    return engine

@pytest.fixture
def pce_engine_3d_plot():
    # Initialize the Input object for the problem
    inp = Input()
    
    # Add marginals for the input dimensions
    inp.add_marginals()
    inp.marginals[0].name = 'x1'
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]  # mean = 0, std = 1
    
    inp.add_marginals()
    inp.marginals[1].name = 'x2'
    inp.marginals[1].dist_type = 'normal'
    inp.marginals[1].parameters = [0, 1]  # mean = 0, std = 1
    
    # Initialize the experimental design
    expdes = ExpDesigns(inp)
    expdes.init_param_space(max_deg=1)  # Define the degree of the polynomial expansion
    
    # Defining the design points and response (output)
    expdes.y = {
        'Z': [[0.4], [0.5], [0.3], [0.4]],
        'Y': [[0.35], [0.45], [0.40], [0.38]]
    }
    expdes.x = np.array([[0,0], [1,0], [0.5,0.3], [0.3,0.7]])
    expdes.x_values = [0] # Example x-values (could be used for visualization or plotting)
    
    # Create and fit the Polynomial Chaos Expansion model (PCE)
    mm = PCE(inp)  # Initialize the PCE model
    mm.fit(expdes.x, expdes.y)  # Fit the model to the design points and outputs
    
    # Define a surrogate model or predictor
    mod = PL() 
    # Initialize the Engine with the metamodel, model, and experimental design
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z', 'Y']  # Define the output names
    engine.emulator = True  # Indicate that the engine is emulating a trained model
    engine.trained = True  # Mark the engine as trained
    
    return engine  # Return the configured engine

@pytest.fixture
def gpe_engine(): 
    inp = Input()
    
    inp.add_marginals()
    inp.marginals[0].name = 'x'
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    
    expdes = ExpDesigns(inp)
    expdes.init_param_space()
    expdes.x = np.array([[0], [1], [0.5]])
    expdes.y = {'Z': [[0.4], [0.5], [0.45]]}
    expdes.x_values = [0]
    
    mm = GPESkl(inp)
    mm.fit(expdes.x, expdes.y)
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    engine.emulator = True
    engine.trained = True
    return engine

#%% Test PostProcessing init

def test_postprocessing_noengine():
    None

def test_postprocessing_untrained_engine(basic_engine) -> None:
    engine = basic_engine
    with pytest.raises(AttributeError) as excinfo:
        PostProcessing(engine)
    assert str(excinfo.value) == 'PostProcessing can only be performed on trained engines.'

def test_postprocessing_no_MetaModel(engine_no_MetaModel) -> None: 
    
    engine = engine_no_MetaModel 
    
    with pytest.raises(AttributeError) as excinfo:
        PostProcessing(engine)
    assert str(excinfo.value) == 'PostProcessing can only be performed on engines with a trained MetaModel.'

def test_postprocessing_pce(pce_engine) -> None:
    engine = pce_engine
    PostProcessing(engine)
    
def test_postprocessing_gpe(gpe_engine) -> None:
    engine = gpe_engine
    PostProcessing(engine)
#%% plot_moments
def test_plot_moments_pce(pce_engine) -> None:
    """
    Plot moments for PCE metamodel
    """
    engine = pce_engine
    post = PostProcessing(engine)
    mean, stdev = post.plot_moments()
    # Check the mean dict
    assert list(mean.keys()) == ['Z']
    assert mean['Z'].shape == (1,)
    assert mean['Z'][0] == pytest.approx(0.4, abs=0.01)
    # Check the stdev dict
    assert list(stdev.keys()) == ['Z']
    assert stdev['Z'].shape == (1,)
    assert stdev['Z'][0] == pytest.approx(0.1, abs=0.01)
    
def test_plot_moments_pcebar(pce_engine) -> None:
    """
    Plot moments for PCE metamodel with bar-plot
    """
    engine = pce_engine
    post = PostProcessing(engine)
    mean, stdev = post.plot_moments(plot_type='bar')
    # Check the mean dict
    assert list(mean.keys()) == ['Z']
    assert mean['Z'].shape == (1,)
    assert mean['Z'][0] == pytest.approx(0.4, abs=0.01)
    # Check the stdev dict
    assert list(stdev.keys()) == ['Z']
    assert stdev['Z'].shape == (1,)
    assert stdev['Z'][0] == pytest.approx(0.1, abs=0.01)
    
def test_plot_moments_gpe(gpe_engine) -> None:
    """
    Plot moments for GPE metamodel
    """
    engine = gpe_engine
    post = PostProcessing(engine)
    mean, stdev = post.plot_moments()
    # Check the mean dict
    assert list(mean.keys()) == ['Z']
    assert mean['Z'].shape == (1,)
    assert mean['Z'][0] == pytest.approx(0.4, abs=0.01)
    # Check the stdev dict
    assert list(stdev.keys()) == ['Z']
    assert stdev['Z'].shape == (1,)
    assert stdev['Z'][0] == pytest.approx(0.1, abs=0.01)

def test_plot_moments_gpebar(gpe_engine) -> None:
    """
    Plot moments for GPE metamodel with bar-plot
    """
    engine = gpe_engine
    post = PostProcessing(engine)
    mean, stdev = post.plot_moments(plot_type='bar')
    # Check the mean dict
    assert list(mean.keys()) == ['Z']
    assert mean['Z'].shape == (1,)
    assert mean['Z'][0] == pytest.approx(0.4, abs=0.01)
    # Check the stdev dict
    assert list(stdev.keys()) == ['Z']
    assert stdev['Z'].shape == (1,)
    assert stdev['Z'][0] == pytest.approx(0.1, abs=0.01)
    
#%% valid_metamodel
def test_valid_metamodel_pce(pce_engine):
    engine = pce_engine
    post = PostProcessing(engine)
    samples = np.array([[0], [1], [0.5]])
    model_out_dict = {'Z': np.array([[0.4], [0.5], [0.45]])}
    post.valid_metamodel(samples=samples, model_out_dict=model_out_dict)

def test_valid_metamodel_gpe(gpe_engine):
    engine = gpe_engine
    post = PostProcessing(engine)
    samples = np.array([[0], [1], [0.5]])
    model_out_dict = {'Z': np.array([[0.4], [0.5], [0.45]])}
    post.valid_metamodel(samples=samples, model_out_dict=model_out_dict)

#%% check_accuracy

def test_check_accuracy_pce(pce_engine) -> None:
    """
    Check accuracy for PCE metamodel 
    """
    engine = pce_engine
    post = PostProcessing(engine)
    post.check_accuracy(samples = engine.exp_design.x, outputs = engine.exp_design.y)

def test_check_accuracy_gpe(gpe_engine) -> None:
    """
    Check accuracy for GPE metamodel
    """
    engine = gpe_engine
    post = PostProcessing(engine)
    post.check_accuracy(samples = engine.exp_design.x, outputs = engine.exp_design.y)
#%% plot_seq_design_diagnoxtics
# def test_plot_seq_design_diagnostics(basic_engine_sequential):
#     """
#     Test the plot_seq_design_diagnostics method
#     """
#     engine = basic_engine_sequential
#     engine.exp_design.n_max_samples = 4
#     engine.exp_design.n_init_samples = 3
    
#     post = PostProcessing(engine)
#     post.plot_seq_design_diagnostics()
#     # Check if the plot was created and saved
#     assert os.path.exists(f"./{post.out_dir}/seq_design_diagnostics/seq_BME.{post.out_format}")
#     assert os.path.exists(f"./{post.out_dir}/seq_design_diagnostics/seq_KLD.{post.out_format}")
#     assert os.path.exists(f"./{post.out_dir}/seq_design_diagnostics/seq_Modified_LOO_error.{post.out_format}")
#     assert os.path.exists(f"./{post.out_dir}/seq_design_diagnostics/seq_RMSEMean.{post.out_format}")
#     assert os.path.exists(f"./{post.out_dir}/seq_design_diagnostics/seq_RMSEStd.{post.out_format}")

#%% sobol_indices

def test_sobol_indices_pce(pce_engine) -> None:
    """
    Calculate sobol indices for PCE metamodel
    """
    engine = pce_engine
    post = PostProcessing(engine)
    sobol, totalsobol = post.sobol_indices()

    assert list(totalsobol.keys()) == ['Z']
    assert totalsobol['Z'].shape == (1,1)
    assert totalsobol['Z'][0,0] == 1

    print(sobol)
    assert list(sobol.keys()) == [1]
    assert list(sobol[1].keys()) == ['Z']
    assert sobol[1]['Z'].shape == (1,1,1)
    assert sobol[1]['Z'][0,0] == 1

def test_sobol_indices_with_invalid_model_type(gpe_engine) -> None:
    """
    Calculate sobol indices with invalid model type
    """
    engine = gpe_engine
    post = PostProcessing(engine)
    post.model_type = 'INVALID'
    with pytest.raises(AttributeError) as excinfo:
        post.sobol_indices()
    assert "Sobol indices only support PCE-type models!" in str(excinfo.value)

#%% check_reg_quality

def test_check_reg_quality_pce(pce_engine) -> None:
    """
    Check the regression quality for PCE metamodel
    """
    engine = pce_engine
    post = PostProcessing(engine)
    post.check_reg_quality(samples=engine.exp_design.x, outputs=engine.exp_design.y)

def test_check_reg_quality_gpe(gpe_engine) -> None:
    """
    Check the regression quality for GPE metamodel
    """
    engine = gpe_engine
    post = PostProcessing(engine)
    post.check_reg_quality(samples=engine.exp_design.x, outputs=engine.exp_design.y)
    # Add assertions to check the quality metrics if available

#%% plot_metamodel_3d
def test_plot_metamodel_3d_pce(pce_engine_3d_plot) -> None:
    """
    Test the plot_metamodel_3d method for PCE metamodel
    """
    engine = pce_engine_3d_plot
    post = PostProcessing(engine)
    post.plot_metamodel_3d()
    # Check if the plot was created and saved
    assert os.path.exists(f"./{post.out_dir}/3DPlot_MetaModel_Z0.{post.out_format}")
    assert os.path.exists(f"./{post.out_dir}/3DPlot_MetaModel_Y0.{post.out_format}")


#%% _plot_validation_multi only for PCE
def test_plot_validation_multi(pce_engine_3d_plot):
    """
    Test the _plot_validation_multi method
    """
    engine = pce_engine_3d_plot
    post = PostProcessing(engine)
    y_val = {'Z': np.array([[1], [2], [3], [4], [5]]),
             'Y': np.array([[1], [2], [3], [4], [5]])}
    y_val_std = {'Z': np.array([[0.1], [0.2], [0.3], [0.4], [0.5]]),
                'Y': np.array([[0.1], [0.2], [0.3], [0.4], [0.5]])}
    model_out = {'Z': np.array([[1.5],[2],[3.5],[4],[4.5]]),
                 'Y': np.array([[1.5],[2],[3.5],[4],[4.5]])}
    post._plot_validation_multi(y_val, y_val_std, model_out)
    # Check if the plot was created and saved
    assert os.path.exists(f"./{post.out_dir}/Model_vs_pceModel_Y.{post.out_format}")
    assert os.path.exists(f"./{post.out_dir}/Model_vs_pceModel_Z.{post.out_format}")

def test_plot_validation_multi_pce(pce_engine):
    engine = pce_engine
    post = PostProcessing(engine)
    out_mean = {'Z': np.array([[0.4], [0.5], [0.45], [0.4]])}
    out_std = {'Z': np.array([[0.1], [0.1], [0.1], [0.1]])}
    model_out_dict = {'Z': np.array([[0.4], [0.5],[0.3],[0.4]])}
    post._plot_validation_multi(out_mean, out_std, model_out_dict)

def test_plot_validation_multi_gpe(gpe_engine):
    engine = gpe_engine
    post = PostProcessing(engine)
    out_mean = {'Z': np.array([[0.4], [0.5], [0.45]])}
    out_std = {'Z': np.array([[0.1], [0.1], [0.1]])}
    model_out_dict = {'Z': np.array([[0.4], [0.5], [0.45]])}
    post._plot_validation_multi(out_mean, out_std, model_out_dict)
