# -*- coding: utf-8 -*-
"""
Tests the class Engine in bayesvalidrox
Engine:
    start_engine         - x
    train_normal
    train_sequential
    eval_metamodel
    train_seq_design
    util_VarBasedDesign
    util_BayesianActiveDesign
    util_BayesianDesign
    run_util_func
    dual_annealing
    tradoff_weights      - x
    choose_next_sample
        plotter
    util_AlphOptDesign
    _normpdf            - x    Also move outside the class?
    _corr_factor_bme           Not used again in this class
    plot_posterior      - x
    _bme_calculator     - x
    _valid_error         - x
    _error_mean_std     - x 

"""
import numpy as np
import pandas as pd
import sys

sys.path.append("../src/")

from bayesvalidrox.surrogate_models.inputs import Input
from bayesvalidrox.surrogate_models.exp_designs import ExpDesigns
from bayesvalidrox.surrogate_models.meta_model import MetaModel
from bayesvalidrox.surrogate_models.polynomial_chaos import PCE
from bayesvalidrox.pylink.pylink import PyLinkForwardModel as PL
from bayesvalidrox.surrogate_models.engine import Engine
from bayesvalidrox.bayes_inference.discrepancy import Discrepancy

import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)

#%% Test Engine constructor


def test_engine() -> None:
    """
    Build Engine without inputs
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mod = PL()
    mm = MetaModel(inp)
    expdes = ExpDesigns(inp)
    Engine(mm, mod, expdes)


#%% Test Engine.start_engine

def test_start_engine() -> None:
    """
    Build Engine without inputs
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mod = PL()
    mm = MetaModel(inp)
    expdes = ExpDesigns(inp)
    engine = Engine(mm, mod, expdes)
    engine.start_engine()


#%% Test Engine.train_normal
# TODO: build mock model to do this? - test again in full-length examples

#%% Test Engine._error_mean_std

def test__error_mean_std_nomc() -> None:
    """
    Compare moments of surrogate and reference without mc-reference
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)
    mm.fit([[0.0], [1.0]], {'Z': [[0.5], [0.5]]})
    expdes = ExpDesigns(inp)
    mod = PL()
    mod.mc_reference['mean'] = [0.5]
    mod.mc_reference['std'] = [0.0]
    mod.output.names = ['Z']
    engine = Engine(mm, mod, expdes)
    engine.start_engine()
    mean, std = engine._error_mean_std()
    assert mean < 0.01 and std < 0.01

    
#def test__error_mean_std() -> None:
#    """
#    Compare moments of surrogate and reference
#    """
#    mod = PL()
#    engine = Engine(None, mod, None)
#    engine.start_engine()
#    with pytest.raises(AttributeError) as excinfo:
#        engine._error_mean_std()
#    assert str(excinfo.value) == ('Model.mc_reference needs to be given to calculate the surrogate error!')

#%% Test Engine._valid_error

def test__valid_error() -> None:
    """
    Calculate validation error
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)
    mm.fit([[0.0], [1.0]], {'Z': [[0.5], [0.5]]})
    expdes = ExpDesigns(inp)
    mod = PL()
    expdes.valid_samples = np.array([[0.5]])
    expdes.valid_model_runs = {'Z': np.array([[0.5]])}
    mod.output.names = ['Z']
    engine = Engine(mm, mod, expdes)
    engine.start_engine()
    rmse, mse = engine._valid_error()
    assert rmse['Z'][0] < 0.01  and np.isnan(mse['Z'][0])


#%% Test Engine._bme_calculator

def test__bme_calculator() -> None:
    """
    Calculate BME
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)
    mm.fit([[0.0], [0.5], [1.0]], {'Z': [[0.5], [0.4], [0.1]]})
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.generate_ed(max_deg=1)
    mod = PL()
    mod.output.names = ['Z']
    engine = Engine(mm, mod, expdes)
    engine.start_engine()
    obs_data = {'Z': np.array([0.45])}
    sigma2Dict = {'Z': np.array([0.05])}
    disc = Discrepancy(parameters = sigma2Dict)
    disc.build_discrepancy()
    engine.discrepancy=disc
    sigma2Dict = pd.DataFrame(sigma2Dict, columns=['Z'])
    engine._bme_calculator(obs_data)
    # Note: if error appears here it might also be due to inoptimal choice of training samples


def test__bme_calculator_rmse() -> None:
    """
    Calculate BME with given RMSE
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = PCE(inp)
    mm.fit([[0.0], [0.5], [1.0]], {'Z': [[0.5], [0.4], [0.5]]})
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.generate_ed(max_deg=1)
    mod = PL()
    mod.output.names = ['Z']
    engine = Engine(mm, mod, expdes)
    engine.start_engine()
    obs_data = {'Z': np.array([0.45])}
    sigma2Dict = {'Z': np.array([0.05])}
    disc = Discrepancy(parameters = sigma2Dict)
    disc.build_discrepancy()
    engine.discrepancy=disc
    sigma2Dict = pd.DataFrame(sigma2Dict, columns=['Z'])
    engine._bme_calculator(obs_data, rmse={'Z': 0.1})
    # Note: if error appears here it might also be due to inoptimal choice of training samples


if 0:
    def test__bme_calculator_lik() -> None:
        """
        Calculate BME with given validation likelihood and post-snapshot
        """
        inp = Input()
        inp.add_marginals()
        inp.marginals[0].dist_type = 'normal'
        inp.marginals[0].parameters = [0, 1]
        mm = PCE(inp)
        mm.fit([[0.0], [0.5], [1.0]], {'Z': [[0.5], [0.4], [0.5]]})
        expdes = ExpDesigns(inp)
        expdes.n_init_samples = 2
        expdes.generate_ed(max_deg=1)
        mod = PL()
        mod.output.names = ['Z']
        engine = Engine(mm, mod, expdes)
        engine.start_engine()

        obs_data = {'Z': np.array([0.45])}
        sigma2Dict = {'Z': np.array([0.05])}
        disc = Discrepancy(parameters = sigma2Dict)
        disc.build_discrepancy()
        engine.discrepancy=disc
        engine.post_snapshot = True
        engine.valid_likelihoods = [0.1]

        engine._bme_calculator(obs_data)


def test__bme_calculator_2d() -> None:
    """
    Calculate BME with given validation likelihood and post-snapshot, 2d input
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    inp.add_marginals()
    inp.marginals[1].dist_type = 'normal'
    inp.marginals[1].parameters = [0, 1]
    mm = PCE(inp)
    mm.fit([[0.0, 0.0], [0.5, 0.1], [1.0, 0.9]], {'Z': [[0.5], [0.4], [0.5]]})
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.generate_ed(max_deg=1)
    mod = PL()
    mod.n_obs = 1
    mod.output.names = ['Z']
    engine = Engine(mm, mod, expdes)
    engine.start_engine()
    obs_data = {'Z': np.array([0.45])}
    sigma2Dict = {'Z': np.array([0.05])}
    disc = Discrepancy(parameters = sigma2Dict)
    disc.build_discrepancy()
    engine.discrepancy=disc
    sigma2Dict = pd.DataFrame(sigma2Dict, columns=['Z'])
    expdes.post_snapshot = True

    engine.valid_likelihoods = [0.1]
    engine._bme_calculator(obs_data)


#%% Test Engine.plot_posterior

def test_plot_posterior() -> None:
    """
    Plot posterior
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mm = MetaModel(inp)
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.generate_ed(max_deg=1)
    mod = PL()
    posterior = np.array([[0], [0.1], [0.2]])
    engine = Engine(mm, mod, expdes)
    engine.plot_posterior(posterior, ['i'], 'Z')


def test_plot_posterior_2d() -> None:
    """
    Plot posterior for 2 params
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    inp.add_marginals()
    inp.marginals[1].dist_type = 'normal'
    inp.marginals[1].parameters = [0, 1]
    mm = MetaModel(inp)
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.generate_ed(max_deg=1)
    mod = PL()
    posterior = np.array([[0, 0], [0.1, 1.0], [0.2, 0.5]])
    engine = Engine(mm, mod, expdes)
    engine.plot_posterior(posterior, ['i', 'j'], 'Z')
