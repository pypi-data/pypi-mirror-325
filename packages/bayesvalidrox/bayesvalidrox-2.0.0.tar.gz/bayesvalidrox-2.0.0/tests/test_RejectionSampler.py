# -*- coding: utf-8 -*-
"""
Test the BayesInference class for bayesvalidrox

Tests are available for the following functions
class RejectionSampler:
    serun_sampler
    calculate_valid_metrics
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
from bayesvalidrox.bayes_inference.rejection_sampler import RejectionSampler


#%% Test MCMC init

def test_RejectionSampler() -> None:
    """
    Construct a RejectionSampler object
    """
    RejectionSampler()

#%% Test rejection_sampling
def test_rejection_sampling_nologlik() -> None:
    """
    Perform rejection sampling without given log likelihood
    """
    rej = RejectionSampler()
    rej.prior_samples = np.array([[0,0,1]])
    rej.log_likes = np.array([[1]])
    rej.run_sampler()
