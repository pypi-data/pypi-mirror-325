import numpy as np
from typing import Any, List


def ate(ite: List[float]) -> float:
    """Unbiased ATE estimator.

    The sample mean of an array of unbiased ITE estimates

    Parameters
    ----------
    ite : list of float

    Returns
    -------
    float
        Average Treatment Effect estimate.
    """
    return np.mean(ite).astype(float)


def check_shrinkage_rate(t: int, delta_t: float):
    """Checks the shrinkage rate delta_t defined in Liang and Bojinov"""
    assert t <= 1 or delta_t > 1 / (
        t ** (1 / 4)
    ), "Sequence is converging to 0 too quickly"


def cs_radius(var: List[float], t: int, t_star: int, alpha: float = 0.05) -> float:
    """
    Confidence sequence radius

    Parameters
    ----------
    var : list of float
        An array-like of individual treatment effect variances (upper bounds).
    t : int
        The current time-step of the algorithm.
    t_star: int
        The time-step at which we want to optimize the CSs to be tightest.
    alpha : float
        The size of the statistical test.

    Returns
    -------
    float
        The radius of the Confidence Sequence. Aka the value V such that
        tau (ATE estimate) ± V is a valid alpha-level CS.
    """
    S = np.sum(var)
    eta = np.sqrt((-2 * np.log(alpha) + np.log(-2 * np.log(alpha) + 1)) / t_star)
    rad = np.sqrt(
        2
        * (S * (eta**2) + 1)
        / ((t**2) * (eta**2))
        * np.log(np.sqrt(S * (eta**2) + 1) / alpha)
    )
    return rad.astype(float)


def ite(outcome: float, treatment: int, propensity: float) -> float:
    """Unbiased individual treatment effect estimator"""
    if treatment == 0:
        ite = -outcome / propensity
    else:
        ite = outcome / propensity
    return ite


def last(x: List[Any]) -> Any:
    """Returns the last element of a list. Returns None if empty list."""
    if len(x) < 1:
        return None
    return x[len(x) - 1]


def var(outcome: float, propensity: float) -> float:
    """Upper bound for individual treatment effect variance"""
    var_ub = (outcome**2) / (propensity**2)
    return var_ub
