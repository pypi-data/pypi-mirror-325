from abc import ABC
from typing import List
import numpy as np
import numpy.typing as npt

try:
    import cupy as cp

    NO_GPU = False

except ImportError:
    NO_GPU = True
    cp = np

from suppy.feasibility._linear_algorithms import HyperslabFeasibility
from suppy.utils import LinearMapping


class HyperslabAMSAlgorithm(HyperslabFeasibility, ABC):
    """
    The HyperslabAMSAlgorithm class is used to find a feasible solution to a
    set of
    linear inequalities.

    Parameters
    ----------
    A : npt.NDArray
        The matrix representing the coefficients of the linear inequalities.
    lb : npt.NDArray
        The lower bounds for the inequalities.
    ub : npt.NDArray
        The upper bounds for the inequalities.
    algorithmic_relaxation : npt.NDArray or float, optional
        The relaxation parameter for the algorithm, by default 1.
    relaxation : float, optional
        The relaxation parameter for the feasibility problem, by default 1.
    proximity_flag : bool, optional
        A flag indicating whether to use proximity in the algorithm, by default True.
    """

    def __init__(
        self,
        A: npt.NDArray,
        lb: npt.NDArray,
        ub: npt.NDArray,
        algorithmic_relaxation: npt.NDArray | float = 1,
        relaxation: float = 1,
        proximity_flag: bool = True,
    ):
        super().__init__(A, lb, ub, algorithmic_relaxation, relaxation, proximity_flag)


class SequentialAMSHyperslab(HyperslabAMSAlgorithm):
    """
    SequentialAMSHyperslab class for sequentially applying the AMS algorithm
    on hyperslabs.

    Parameters
    ----------
    A : npt.NDArray
        The matrix A used in the AMS algorithm.
    lb : npt.NDArray
        The lower bounds for the constraints.
    ub : npt.NDArray
        The upper bounds for the constraints.
    algorithmic_relaxation : npt.NDArray or float, optional
        The relaxation parameter for the algorithm, by default 1.
    relaxation : float, optional
        The relaxation parameter, by default 1.
    cs : None or List[int], optional
        The list of indices for the constraints, by default None.
    proximity_flag : bool, optional
        Flag to indicate if proximity should be considered, by default True.
    """

    def __init__(
        self,
        A: npt.NDArray,
        lb: npt.NDArray,
        ub: npt.NDArray,
        algorithmic_relaxation: npt.NDArray | float = 1,
        relaxation: float = 1,
        cs: None | List[int] = None,
        proximity_flag: bool = True,
    ):

        super().__init__(A, lb, ub, algorithmic_relaxation, relaxation, proximity_flag)
        xp = cp if self._use_gpu else np
        if cs is None:
            self.cs = xp.arange(self.A.shape[0])
        else:
            self.cs = cs

    def _project(self, x: npt.NDArray) -> npt.NDArray:
        """
        Projects the input array `x` onto the feasible region defined by the
        constraints.

        Parameters
        ----------
        x : npt.NDArray
            The input array to be projected.

        Returns
        -------
        npt.NDArray
            The projected array.
        """

        for i in self.cs:
            p_i = self.single_map(x, i)
            (res_li, res_ui) = self.bounds.single_residual(p_i, i)  # returns floats
            # check if constraints are violated

            # weights should be 1s!
            if res_ui < 0:
                self.A.update_step(
                    x, self.algorithmic_relaxation * self.inverse_row_norm[i] * res_ui, i
                )
            elif res_li < 0:
                self.A.update_step(
                    x, -1 * self.algorithmic_relaxation * self.inverse_row_norm[i] * res_li, i
                )
        return x


class SequentialWeightedAMSHyperslab(SequentialAMSHyperslab):
    """
    Parameters
    ----------
    A : npt.NDArray
        The constraint matrix.
    lb : npt.NDArray
        The lower bounds of the constraints.
    ub : npt.NDArray
        The upper bounds of the constraints.
    weights : None, list of float, or npt.NDArray, optional
        The weights assigned to each constraint. If None, default weights are
    used.
    algorithmic_relaxation : npt.NDArray or float, optional
        The relaxation parameter for the algorithm. Default is 1.
    relaxation : float, optional
        The relaxation parameter for the algorithm. Default is 1.
    weight_decay : float, optional
        Parameter that determines the rate at which the weights are reduced
    after each phase (weights * weight_decay). Default is 1.
    cs : None or list of int, optional
        The indices of the constraints to be considered. Default is None.
    proximity_flag : bool, optional
        Flag to indicate if proximity should be considered. Default is True.

    Attributes
    ----------
    weights : npt.NDArray
        The weights assigned to each constraint.
    weight_decay : float
        Decay rate for the weights.
    temp_weight_decay : float
        Initial value for weight decay.
    """

    def __init__(
        self,
        A: npt.NDArray,
        lb: npt.NDArray,
        ub: npt.NDArray,
        weights: None | List[float] | npt.NDArray = None,
        algorithmic_relaxation: npt.NDArray | float = 1,
        relaxation: float = 1,
        weight_decay: float = 1,
        cs: None | List[int] = None,
        proximity_flag: bool = True,
    ):

        super().__init__(A, lb, ub, algorithmic_relaxation, relaxation, cs, proximity_flag)
        xp = cp if self._use_gpu else np
        self.weight_decay = weight_decay  # decay rate
        self.temp_weight_decay = 1  # initial value for weight decay

        if weights is None:
            self.weights = xp.ones(self.A.shape[0])
        elif xp.abs((weights.sum() - 1)) > 1e-10:
            print("Weights do not add up to 1! Renormalizing to 1...")
            self.weights = weights

    def _project(self, x: npt.NDArray) -> npt.NDArray:
        """
        Projects the input array `x` onto a feasible region defined by the
        constraints.

        Parameters
        ----------
        x : npt.NDArray
            The input array to be projected.

        Returns
        -------
        npt.NDArray
            The projected array.

        Notes
        -----
        This method iteratively adjusts the input array `x` based on the constraints
        defined in `self.cs`. For each constraint, it computes the projection and
        checks if the constraints are violated. If a constraint is violated, it updates
        the array `x` using a weighted relaxation factor. The weight decay is applied
        to the temporary weight decay after each iteration.
        """

        weighted_relaxation = self.algorithmic_relaxation * self.temp_weight_decay

        for i in self.cs:

            p_i = self.single_map(x, i)

            (res_li, res_ui) = self.bounds.single_residual(p_i, i)  # returns floats
            # check if constraints are violated

            if res_ui < 0:
                self.A.update_step(
                    x, weighted_relaxation * self.weights[i] * self.inverse_row_norm[i] * res_ui, i
                )
            elif res_li < 0:
                self.A.update_step(
                    x,
                    -1 * weighted_relaxation * self.weights[i] * self.inverse_row_norm[i] * res_li,
                    i,
                )

        self.temp_weight_decay *= self.weight_decay
        return x


class SimultaneousAMSHyperslab(HyperslabAMSAlgorithm):
    """
    SimultaneousAMSHyperslab class for simultaneous application of the AMS
    algorithm on hyperslabs.

    Parameters
    ----------
    A : npt.NDArray
        The matrix representing the constraints.
    lb : npt.NDArray
        The lower bounds for the constraints.
    ub : npt.NDArray
        The upper bounds for the constraints.
    algorithmic_relaxation : npt.NDArray or float, optional
        The relaxation parameter for the algorithm, by default 1.
    relaxation : float, optional
        The relaxation parameter for the projections, by default 1.
    weights : None or List[float], optional
        The weights for the constraints, by default None.
    proximity_flag : bool, optional
        Flag to indicate if proximity calculations should be performed, by default True.
    """

    def __init__(
        self,
        A: npt.NDArray,
        lb: npt.NDArray,
        ub: npt.NDArray,
        algorithmic_relaxation: npt.NDArray | float = 1,
        relaxation: float = 1,
        weights: None | List[float] = None,
        proximity_flag: bool = True,
    ):

        super().__init__(A, lb, ub, algorithmic_relaxation, relaxation, proximity_flag)

        xp = cp if self._use_gpu else np

        if weights is None:
            self.weights = xp.ones(self.A.shape[0]) / self.A.shape[0]
        elif xp.abs((weights.sum() - 1)) > 1e-10:
            print("Weights do not add up to 1! Renormalizing to 1...")
            self.weights = weights / weights.sum()
        else:
            self.weights = weights

    def _project(self, x):
        # simultaneous projection
        p = self.map(x)
        (res_l, res_u) = self.bounds.residual(p)
        d_idx = res_u < 0
        c_idx = res_l < 0
        x += self.algorithmic_relaxation * (
            (self.weights * self.inverse_row_norm)[d_idx] * res_u[d_idx] @ self.A[d_idx, :]
            - (self.weights * self.inverse_row_norm)[c_idx] * res_l[c_idx] @ self.A[c_idx, :]
        )

        return x

    def _proximity(self, x: npt.NDArray, proximity_measures: List[str]) -> float:
        p = self.map(x)
        # residuals are positive if constraints are met
        (res_l, res_u) = self.bounds.residual(p)
        res_u[res_u > 0] = 0
        res_l[res_l > 0] = 0
        res = -res_u - res_l
        measures = []
        for measure in proximity_measures:
            if isinstance(measure, tuple):
                if measure[0] == "p_norm":
                    measures.append(self.weights @ (res ** measure[1]))
                else:
                    raise ValueError("Invalid proximity measure")
            elif isinstance(measure, str) and measure == "max_norm":
                measures.append(res.max())
            else:
                raise ValueError("Invalid proximity measure)")
        return measures


class ExtrapolatedLandweber(SimultaneousAMSHyperslab):
    def __init__(
        self, A, lb, ub, algorithmic_relaxation=1, relaxation=1, weights=None, proximity_flag=True
    ):
        super().__init__(A, lb, ub, algorithmic_relaxation, relaxation, weights, proximity_flag)
        self.a_i = self.A.row_norm(2, 2)
        self.weight_norm = self.weights / self.a_i
        self.sigmas = []

    def _project(self, x):
        xp = cp if self._use_gpu else np
        p = self.map(x)
        (res_l, res_u) = self.bounds.residual(p)
        d_idx = res_u < 0
        c_idx = res_l < 0
        if not (xp.any(d_idx) or xp.any(c_idx)):
            self.sigmas.append(0)
            return x
        t_u = self.weight_norm[d_idx] * res_u[d_idx]  # D*(Ax-b)+
        t_l = self.weight_norm[c_idx] * res_l[c_idx]
        t_u_2 = t_u @ self.A[d_idx, :]
        t_l_2 = t_l @ self.A[c_idx, :]

        sig = ((res_l[c_idx] @ (t_l)) + (res_u[d_idx] @ (t_u))) / (
            (t_u_2 - t_l_2) @ (t_u_2 - t_l_2)
        )
        self.sigmas.append(sig)
        x += sig * (t_u_2 - t_l_2)

        return x


class BlockIterativeAMSHyperslab(HyperslabAMSAlgorithm):
    """
    Block Iterative AMS Algorithm for hyperslabs.

    Parameters
    ----------
    A : npt.NDArray
        The matrix representing the linear constraints.
    lb : npt.NDArray
        The lower bounds for the constraints.
    ub : npt.NDArray
        The upper bounds for the constraints.
    weights : List[List[float]] or List[npt.NDArray]
        A list of lists or arrays representing the weights for each block. Each list/array should sum to 1.
    algorithmic_relaxation : npt.NDArray or float, optional
        The relaxation parameter for the algorithm, by default 1.
    relaxation : float, optional
        The relaxation parameter for the constraints, by default 1.
    proximity_flag : bool, optional
        A flag indicating whether to use proximity measures, by default True.

    Raises
    ------
    ValueError
        If any of the weight lists do not sum to 1.
    """

    def __init__(
        self,
        A: npt.NDArray,
        lb: npt.NDArray,
        ub: npt.NDArray,
        weights: List[List[float]] | List[npt.NDArray],
        algorithmic_relaxation: npt.NDArray | float = 1,
        relaxation: float = 1,
        proximity_flag: bool = True,
    ):

        super().__init__(A, lb, ub, algorithmic_relaxation, relaxation, proximity_flag)

        xp = cp if self._use_gpu else np

        # check that weights is a list of lists that add up to 1 each
        for el in weights:
            if xp.abs((xp.sum(el) - 1)) > 1e-10:
                raise ValueError("Weights do not add up to 1!")

        self.weights = []
        self.block_idxs = [
            xp.where(xp.array(el) > 0)[0] for el in weights
        ]  # get idxs that meet requirements

        # assemble a list of general weights
        self.total_weights = xp.zeros_like(weights[0])
        for el in weights:
            el = xp.asarray(el)
            self.weights.append(el[xp.array(el) > 0])  # remove non zero weights
            self.total_weights += el / len(weights)

    def _project(self, x):
        # simultaneous projection
        xp = cp if self._use_gpu else np

        for el, block_idx in zip(self.weights, self.block_idxs):  # get mask and associated weights
            p = self.indexed_map(x, block_idx)
            (res_l, res_u) = self.bounds.indexed_residual(p, block_idx)
            d_idx = res_u < 0
            c_idx = res_l < 0
            full_d_idx = block_idx[d_idx]
            full_c_idx = block_idx[c_idx]

            x += self.algorithmic_relaxation * (
                self.inverse_row_norm[full_d_idx]
                * el[d_idx]
                * res_u[d_idx]
                @ self.A[full_d_idx, :]
                - self.inverse_row_norm[full_c_idx]
                * el[c_idx]
                * res_l[c_idx]
                @ self.A[full_c_idx, :]
            )

        return x

    def _proximity(self, x: npt.NDArray, proximity_measures: List[str]) -> float:
        p = self.map(x)
        # residuals are positive if constraints are met
        (res_l, res_u) = self.bounds.residual(p)
        res_u[res_u > 0] = 0
        res_l[res_l > 0] = 0
        res = -res_u - res_l
        measures = []
        for measure in proximity_measures:
            if isinstance(measure, tuple):
                if measure[0] == "p_norm":
                    measures.append(self.total_weights @ (res ** measure[1]))
                else:
                    raise ValueError("Invalid proximity measure")
            elif isinstance(measure, str) and measure == "max_norm":
                measures.append(res.max())
            else:
                raise ValueError("Invalid proximity measure)")
        return measures


class StringAveragedAMSHyperslab(HyperslabAMSAlgorithm):
    """
    StringAveragedAMSHyperslab is a string averaged implementation of the
    AMS algorithm.

    Parameters
    ----------
    A : npt.NDArray
        The matrix A used in the algorithm.
    lb : npt.NDArray
        The lower bounds for the variables.
    ub : npt.NDArray
        The upper bounds for the variables.
    strings : List[List[int]]
        A list of lists, where each inner list represents a string of indices.
    algorithmic_relaxation : npt.NDArray or float, optional
        The relaxation parameter for the algorithm, by default 1.
    relaxation : float, optional
        The relaxation parameter for the projection, by default 1.
    weights : None or List[float], optional
        The weights for each string, by default None. If None, equal weights are assigned.
    proximity_flag : bool, optional
        A flag indicating whether to use proximity, by default True.
    """

    def __init__(
        self,
        A: npt.NDArray,
        lb: npt.NDArray,
        ub: npt.NDArray,
        strings: List[List[int]],
        algorithmic_relaxation: npt.NDArray | float = 1,
        relaxation: float = 1,
        weights: None | List[float] = None,
        proximity_flag: bool = True,
    ):

        super().__init__(A, lb, ub, algorithmic_relaxation, relaxation, proximity_flag)
        xp = cp if self._use_gpu else np
        self.strings = strings
        if weights is None:
            self.weights = xp.ones(len(strings)) / len(strings)

        # if check_weight_validity(weights):
        #    self.weights = weights
        else:
            if len(weights) != len(self.strings):
                raise ValueError("The number of weights must be equal to the number of strings.")

            self.weights = weights
            # print('Choosing default weight vector...')
            # self.weights = np.ones(self.A.shape[0])/self.A.shape[0]

    def _project(self, x):
        # string averaged projection
        x_c = x.copy()  # create a general copy of x
        x -= x  # reset x is this viable?
        for string, weight in zip(self.strings, self.weights):
            x_s = x_c.copy()  # generate a copy for individual strings
            for i in string:
                p_i = self.single_map(x_s, i)
                (res_li, res_ui) = self.bounds.single_residual(p_i, i)
                if res_ui < 0:
                    self.A.update_step(
                        x_s, self.algorithmic_relaxation * self.inverse_row_norm[i] * res_ui, i
                    )
                elif res_li < 0:
                    self.A.update_step(
                        x_s,
                        -1 * self.algorithmic_relaxation * self.inverse_row_norm[i] * res_li,
                        i,
                    )

            x += weight * x_s
        return x
