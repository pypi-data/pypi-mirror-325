# -*- coding: utf-8 -*-
"""
Test the Discrepancy class in bayesvalidrox.
Tests are available for the following functions
Class Discrepancy: 
    get_sample

"""
import sys
import pandas as pd
import numpy as np
sys.path.append("src/")
import pytest

from bayesvalidrox.bayes_inference.discrepancy import Discrepancy
from bayesvalidrox.surrogate_models.inputs import Input

#%% Test Discrepancy init

def test_discrepancy() -> None:
    """
    Construct a Discrepancy object
    """
    disc = Discrepancy()
    
#%% Test Discrepancy.build_discrepancy
def test_build_discrepancy_df() -> None:
    """
    Build discrepancy for given dataframe.
    """
    observations = {'Z': np.array([0.45]), 'x_values': np.array([0])}
    names = ['Z']

    obsData = pd.DataFrame(observations, columns=names)
    disc = Discrepancy('Gaussian',(obsData * 0.15) ** 2)
    disc.build_discrepancy()


def test_build_discrepancy_dict() -> None:
    """
    Build discrepancy for given dict.
    """
    observations = {'Z': np.array([0.45]), 'x_values': np.array([0])}
    disc = Discrepancy('Gaussian',observations)
    disc.build_discrepancy()
