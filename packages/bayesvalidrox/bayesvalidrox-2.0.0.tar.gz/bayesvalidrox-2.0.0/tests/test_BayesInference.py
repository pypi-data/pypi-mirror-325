# -*- coding: utf-8 -*-
"""
Test the BayesInference class for bayesvalidrox

Tests are available for the following functions
class BayesInference:
    setup         - x
    run_inference        - x
    run_validation        - x
    _eval_engine
    _eval_model
    get_surr_error
    perturb_data           - x
    calculate_loglik_logbme
    calculate_valid_metrics
    posterior_predictive   - x
    write_as_hdf5
    plot_max_a_posteriori  
    plot_post_params        - x 
    plot_log_BME            - x
    plot_post_predictive   - x
"""

import sys
import pytest
import numpy as np
import pandas as pd

sys.path.append("src/")
sys.path.append("../src/")

from bayesvalidrox.surrogate_models.inputs import Input
from bayesvalidrox.surrogate_models.exp_designs import ExpDesigns
from bayesvalidrox.surrogate_models.meta_model import MetaModel
from bayesvalidrox.surrogate_models.polynomial_chaos import PCE
from bayesvalidrox.pylink.pylink import PyLinkForwardModel as PL
from bayesvalidrox.surrogate_models.engine import Engine
from bayesvalidrox.bayes_inference.discrepancy import Discrepancy
from bayesvalidrox.bayes_inference.mcmc import MCMC
from bayesvalidrox.bayes_inference.bayes_inference import BayesInference


@pytest.fixture
def basic_engine_trained():
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]

    expdes = ExpDesigns(inp, sampling_method='user')
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.x = np.array([[0], [1], [0.5]])
    expdes.y = {'Z': [[0.4], [0.5], [0.45]]}
    expdes.x_values = np.array([0])

    mm = PCE(inp)
    mod = PL()
    mod.observations = {'Z': np.array([0.45]), 'x_values': np.array([0])}
    mod.output.names = ['Z']

    engine = Engine(mm, mod, expdes)
    engine.train_normal()

    return engine

#%% Test MCMC init

def test_BayesInference() -> None:
    """
    Construct a BayesInference object
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]
    mod = PL()
    mm = MetaModel(inp)
    expdes = ExpDesigns(inp)
    engine = Engine(mm, mod, expdes)
    BayesInference(engine)


#%% Test setup

def test_setup_noobservation() -> None:
    """
    Test the object setup without given observations
    """
    inp = Input()
    inp.add_marginals()
    inp.marginals[0].dist_type = 'normal'
    inp.marginals[0].parameters = [0, 1]

    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2

    mm = MetaModel(inp)
    mm.n_params = 1
    expdes.generate_ed(max_deg=np.max(1))

    mod = PL()
    mod.output.names = ['Z']

    engine = Engine(mm, mod, expdes)

    obsData = pd.DataFrame(mod.observations, columns=mod.output.names)
    DiscrepancyOpts = Discrepancy('')
    DiscrepancyOpts.type = 'Gaussian'
    DiscrepancyOpts.parameters = (obsData * 0.15) ** 2

    bi = BayesInference(engine)
    bi.discrepancy = DiscrepancyOpts
    with pytest.raises(Exception) as excinfo:
        bi.setup()
    assert str(
        excinfo.value) == ('Please provide the observation data as a dictionary via observations attribute or pass the '
                           'csv-file path to MeasurementFile attribute')


def test_setup(basic_engine_trained) -> None:
    """
    Test the object setup with observations
    """
    engine = basic_engine_trained
    mod = PL()
    mod.observations = {'Z': np.array([0.45]), 'x_values': np.array([0])}
    mod.output.names = ['Z']

    obsData = pd.DataFrame(mod.observations, columns=mod.output.names)
    DiscrepancyOpts = Discrepancy('')
    DiscrepancyOpts.type = 'Gaussian'
    DiscrepancyOpts.parameters = (obsData * 0.15) ** 2

    bi = BayesInference(engine)
    bi.discrepancy = DiscrepancyOpts
    bi.setup()


def test_setup_priorsamples(basic_engine_trained) -> None:
    """
    Test the object setup with prior samples set by hand
    """
    engine = basic_engine_trained
    mod = PL()
    mod.observations = {'Z': np.array([0.45]), 'x_values': np.array([0])}
    mod.output.names = ['Z']

    obsData = pd.DataFrame(mod.observations, columns=mod.output.names)
    DiscrepancyOpts = Discrepancy('')
    DiscrepancyOpts.type = 'Gaussian'
    DiscrepancyOpts.parameters = (obsData * 0.15) ** 2

    bi = BayesInference(engine)
    bi.prior_samples = np.swapaxes(np.array([np.random.normal(0, 1, 100)]), 0, 1)
    bi.discrepancy = DiscrepancyOpts
    bi.setup()


def test_setup_valid(basic_engine_trained) -> None:
    """
    Test the object setup for valid
    """
    engine=basic_engine_trained
    engine.model.observations_valid = {'Z': np.array([0.45]), 'x_values': np.array([0])}
    # TODO: check for thrown error if observations_valid not given

    obsData = pd.DataFrame(engine.model.observations_valid, columns=engine.out_names)
    disc = Discrepancy('Gaussian',(obsData * 0.15) ** 2)

    bi = BayesInference(engine)
    bi.discrepancy = disc
    bi.name = 'valid'
    bi.setup()


def test_setup_noname(basic_engine_trained) -> None:
    """
    Test the object setup for an invalid inference name
    """
    engine=basic_engine_trained

    bi = BayesInference(engine)
    bi.name = ''
    with pytest.raises(Exception) as excinfo:
        bi.setup()
    assert str(excinfo.value) == 'The set inference type is not known! Use either `calib` or `valid`'


#%% Test run_inference
# TODO: disabled this test!
def test_run_inference(basic_engine_trained) -> None:
    """
    Run inference
    """
    engine = basic_engine_trained
    mod = PL()
    mod.observations = {'Z': np.array([0.45]), 'x_values': np.array([0])}
    mod.output.names = ['Z']

    obsData = pd.DataFrame(mod.observations, columns=mod.output.names)
    disc = Discrepancy('Gaussian',(obsData * 0.15) ** 2)

    bi = BayesInference(engine)
    bi.discrepancy = disc
    bi.plot = False
    bi.run_inference()


#%% Test _perturb_data
def test_perturb_data_standard(basic_engine_trained) -> None:
    """
    Perturb data
    """
    engine=basic_engine_trained

    bi = BayesInference(engine)
    data = pd.DataFrame()
    data['Z'] = [0.45]
    bi.n_bootstrap_itrs=3
    bi.perturb_data(data, ['Z'])
    # TODO: check e.g. size of perturbed data


def test_perturb_data_loocv(basic_engine_trained) -> None:
    """
    Perturb data with bayes_loocv
    """
    engine=basic_engine_trained

    bi = BayesInference(engine)
    data = pd.DataFrame()
    data['Z'] = [0.45]
    bi.bootstrap_method = 'loocv'
    bi.perturb_data(data, ['Z'])
    # TODO: check e.g. size of perturbed data

def test_perturb_data_none(basic_engine_trained) -> None:
    """
    Run perturbation without actual perturbation
    """
    engine=basic_engine_trained

    bi = BayesInference(engine)
    data = pd.DataFrame()
    data['Z'] = [0.45]
    bi.bootstrap_method = 'none'
    dat = bi.perturb_data(data, ['Z'])
    # TODO: check for match between dat and data


#%% Test _eval_model

def test_eval_model() -> None:
    """
    Run model with descriptive key
    """
    # TODO: need functioning example model to test this
    None


#%% Test _posterior_predictive

def test_posterior_predictive(basic_engine_trained) -> None:
    """
    Test posterior predictions
    """
    engine = basic_engine_trained
    observations = {'Z': np.array([0.45]), 'x_values': np.array([0])}
    names = ['Z']

    obsData = pd.DataFrame(observations, columns=names)
    disc = Discrepancy('Gaussian',(obsData * 0.15) ** 2)
    disc.build_discrepancy()

    posterior = pd.DataFrame()
    posterior[None] = [0, 1, 0.5]

    bi = BayesInference(engine)
    bi.discrepancy = disc
    bi.posterior_df = posterior
    bi.posterior_predictive()



#%% Test plot_post_params

def test_plot_post_params(basic_engine_trained) -> None:
    """
    Plot posterior dist
    """
    engine = basic_engine_trained

    bi = BayesInference(engine)
    posterior = pd.DataFrame()
    posterior[None] = [0, 1, 0.5]
    bi.posterior_df = posterior
    bi.plot_post_params()


def test_plot_post_params_noemulator(basic_engine_trained) -> None:
    """
    Plot posterior dist with emulator = False
    """
    engine = basic_engine_trained

    bi = BayesInference(engine)
    posterior = pd.DataFrame()
    posterior[None] = [0, 1, 0.5]
    bi.posterior_df = posterior
    bi.emulator = False
    bi.plot_post_params()


#%% Test plot_log_BME

def test_plot_logbme(basic_engine_trained) -> None:
    """
    Show the log_BME from bootstrapping
    """
    engine = basic_engine_trained

    bi = BayesInference(engine)
    bi.log_bme = np.array([0, 0.2, 0, 0.2])
    bi.n_tot_measurement = 1
    bi.plot_logbme()


def test_plot_log_BME_noemulator(basic_engine_trained) -> None:
    """
    Show the log_BME from bootstrapping with emulator = False
    """
    engine = basic_engine_trained

    bi = BayesInference(engine)
    bi.log_bme = np.array([0, 0.2, 0, 0.2])
    bi.n_tot_measurement = 1
    bi.emulator = False
    bi.plot_logbme()


#%% Test _plot_max_a_posteriori

if 0:
    def test_plot_max_a_posteriori_rejection(basic_engine_trained) -> None:
        """
        Plot MAP estimate for rejection
        """
        engine=basic_engine_trained
        observations = {'Z': np.array([0.45]), 'x_values': np.array([0])}
        names = ['Z']

        obsData = pd.DataFrame(observations, columns=names)
        disc = Discrepancy('Gaussian',(obsData * 0.15) ** 2)
        disc.build_discrepancy()

        bi = BayesInference(engine)
        bi.discrepancy=disc
        bi.inference_method = 'rejection'
        posterior = pd.DataFrame()
        posterior[None] = [0, 1, 0.5]
        bi.posterior_df = posterior
        bi.measured_data=observations
        bi.plot_max_a_posteriori()


    def test_plot_max_a_posteriori(basic_engine_trained) -> None:
        """
        Plot MAP estimate
        """
        engine=basic_engine_trained

        bi = BayesInference(engine)
        bi.plot_post_predictive()


    #%% Test _plot_post_predictive


    def test_plot_post_predictive_rejection(basic_engine_trained) -> None:
        """
        Plot posterior predictions for rejection
        """
        engine=basic_engine_trained
        observations = {'Z': np.array([0.45]), 'x_values': np.array([0])}
        names = ['Z']

        obsData = pd.DataFrame(observations, columns=names)
        disc = Discrepancy('Gaussian',(obsData * 0.15) ** 2)
        disc.build_discrepancy()

        bi = BayesInference(engine)
        bi.inference_method = 'rejection'
        bi.discrepancy=disc
        bi.measured_data=observations
        bi.plot_post_predictive()


    def test_plot_post_predictive(basic_engine_trained) -> None:
        """
        Plot posterior predictions
        """
        engine=basic_engine_trained
        observations = {'Z': np.array([0.45]), 'x_values': np.array([0])}
        names = ['Z']

        obsData = pd.DataFrame(observations, columns=names)
        disc = Discrepancy('Gaussian',(obsData * 0.15) ** 2)
        disc.build_discrepancy()

        bi = BayesInference(engine)
        bi.discrepancy=disc
        bi.measured_data=observations
        bi.plot_post_predictive()
