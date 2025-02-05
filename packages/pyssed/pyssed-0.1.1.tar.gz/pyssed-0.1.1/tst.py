import numpy as np
import pandas as pd
import plotnine as pn
from pyssed import Bandit, MAD
from typing import Callable, Dict

generator = np.random.default_rng(seed=123)

# Construct bandit instance
class TSBernoulli(Bandit):
    """
    A class for implementing Thompson Sampling on Bernoulli data
    """
    def __init__(self, k: int, control: int, reward: Callable[[int], float]):
        self._active_arms = [x for x in range(k)]
        self._control = control
        self._k = k
        self._means = {x: 0. for x in range(k)}
        self._params = {x: {"alpha": 1, "beta": 1} for x in range(k)}
        self._rewards = {x: [] for x in range(k)}
        self._reward_fn = reward
        self._t = 1
    
    def calculate_probs(self) -> Dict[int, float]:
        samples = np.column_stack([
            np.random.beta(
                a=self._params[idx]["alpha"],
                b=self._params[idx]["beta"],
                size=1000
            )
            for idx in self._active_arms
        ])
        max_indices = np.argmax(samples, axis=1)
        win_counts = {
            idx: np.sum(max_indices == i) / 1000
            for i, idx in enumerate(self._active_arms)
        }
        return win_counts

    def control(self) -> int:
        return self._control
    
    def eliminate_arm(self, arm: int) -> None:
        self._active_arms.remove(arm)
        self._k -= 1
    
    def k(self) -> int:
        return self._k
    
    def probabilities(self) -> Dict[int, float]:
        assert self.k() == len(self._active_arms), "Mismatch in `len(self._active_arms)` and `self.k()`"
        probs = self.calculate_probs()
        return probs
    
    def reactivate_arm(self, arm: int) -> None:
        self._active_arms.append(arm)
        self._active_arms.sort()
        self._k += 1
    
    def reward(self, arm: int) -> float:
        outcome = self._reward_fn(arm)
        self._rewards[arm].append(outcome)
        if outcome == 1:
            self._params[arm]["alpha"] += 1
        else:
            self._params[arm]["beta"] += 1
        self._means[arm] = (
            self._params[arm]["alpha"]
            /(self._params[arm]["alpha"] + self._params[arm]["beta"])
        )
        return outcome

    def t(self) -> int:
        step = self._t
        self._t += 1
        return step

# Run a MAD experiment
def reward_fn(arm: int) -> float:
    values = {
        0: generator.binomial(1, 0.5),  # Control arm
        1: generator.binomial(1, 0.6),  # ATE = 0.1
        2: generator.binomial(1, 0.7), # ATE = 0.2
        3: generator.binomial(1, 0.72),  # ATE = 0.22
    }
    return values[arm]

# MAD algorithm
exp_simple = MAD(
    bandit=TSBernoulli(k=4, control=0, reward=reward_fn),
    alpha=0.05,
    delta=lambda x: 1./(x**0.24),
    t_star=int(20e3)
)
exp_simple.fit(verbose=True)

# Test methods
exp_simple.estimates()
exp_simple.summary()
(
    exp_simple.plot_ate()
    + pn.coord_cartesian(ylim=(-.5, 1.0))
    + pn.geom_hline(
        mapping=pn.aes(yintercept="ate", color="factor(arm)"),
        data=pd.DataFrame({"arm": [1, 2, 3], "ate": [0.1, 0.2, 0.22]}),
        linetype="dotted"
    )
    + pn.theme(strip_text=pn.element_blank())
)
exp_simple.plot_sample_assignment()
exp_simple.plot_n()
