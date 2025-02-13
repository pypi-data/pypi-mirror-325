from dataclasses import dataclass, field
from typing import Optional, Callable, Union
import warnings

import numpy as np
from numpy.typing import NDArray

from .time_series import TimeSeries


MAX_CONDITION_NUMBER = 10


class InstabilityWarning(Warning):

    pass


@dataclass
class EchoStateNetwork:

    """
    ESN class for making prediction
    """

    reservoir_dimensionality: int
    input_dimensionality: int
    w_in: Optional[NDArray] = None
    regularization_parameter: float = 1.0e-10
    generator: Optional[np.random.Generator] = None
    activation_function: Callable[[NDArray], NDArray] = np.tanh
    w_out: NDArray = field(init=False)
    feedback_loop_guess: Union[float, NDArray] = field(init=False)
    timestep: float = field(init=False)
    final_time: float = field(init=False)

    def __post_init__(self):

        """
        Need to initialize a generator and a W_in.
        The generator attribute here is responsible for random sampling
        """

        if not self.generator:
            self.generator = np.random.default_rng(seed=0)

        if self.w_in is None:
            self.w_in = self.generator.uniform(
                low=-0.5,
                high=0.5,
                size=(self.reservoir_dimensionality, self.input_dimensionality)
            )

    def train(self, input_time_series: TimeSeries, pinv: bool = False):

        """
        solve argmin_W ||Y - WX||^2 + λ||W||^2
        """

        # assert that all timesteps are constant
        self.timestep = input_time_series.timestep
        self.final_time = input_time_series.times[-1]

        time_series_array = input_time_series.dependent_variable
        independent_variables = self.activation_function(self.w_in @ time_series_array[:-1, :].T).T
        dependent_variables = time_series_array[1:]

        regularization = self.regularization_parameter * np.eye(independent_variables.shape[1])

        if pinv:
            w_out_transpose = np.linalg.pinv(independent_variables) @ dependent_variables
        else:
            x = independent_variables.T @ independent_variables + regularization

            # conditional number 
            cond_num = np.linalg.cond(x)
            if cond_num > MAX_CONDITION_NUMBER:
                warnings.warn(
                    f"Condition Number {cond_num:.2E} is greater than {MAX_CONDITION_NUMBER}. "
                    f"consider passing pinv = True in {self.__class__.__name__}.train() "
                    f"or increasing {self.__class__.__name__}.regularization_parameter",
                    InstabilityWarning
                )

            w_out_transpose = np.linalg.solve(
                x,
                independent_variables.T @ dependent_variables
            )
            
        self.w_out = w_out_transpose.T
        self.feedback_loop_guess = time_series_array[-1]

    def predict(self, horizon: int) -> TimeSeries:

        """
        Prediction method.
        Need to perform feedback loop, predicting and then feeding prediction back into ESN.
        Predicts the next n steps (horizon) after initial guess.
        Usually, initial guess should be last known training value.
        """

        if self.w_out is None or self.w_in is None:
            raise ValueError("need to train before predicting")

        # initialize predictions and reservoir states to populate later
        predictions = np.zeros((horizon, self.input_dimensionality))

        # perform feedback loop
        for i in range(horizon):
            if i == 0:
                predictions[i, :] = self.w_out @ self.activation_function(self.w_in @ self.feedback_loop_guess)
                continue
            predictions[i, :] = self.w_out @ self.activation_function(self.w_in @ predictions[i - 1, :])

        return TimeSeries(
            dependent_variable=predictions,
            times=self.final_time + self.timestep + np.linspace(0, horizon * self.timestep, horizon)
        )
