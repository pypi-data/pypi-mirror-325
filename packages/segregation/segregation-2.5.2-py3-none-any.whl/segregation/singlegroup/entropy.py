"""Entropy Segregation Index."""

__author__ = "Renan X. Cortes <renanc@ucr.edu>, Sergio J. Rey <sergio.rey@ucr.edu> and Elijah Knaap <elijah.knaap@ucr.edu>"

import geopandas as gpd
import numpy as np

np.seterr(divide="ignore", invalid="ignore")

from .._base import SingleGroupIndex, SpatialImplicitIndex


def _entropy(data, group_pop_var, total_pop_var):
    """Calculate Entropy index.

    Parameters
    ----------
    data : pandas.DataFrame or geopandas.GeoDataFrame
        Dataframe or geodataframe if spatial index holding data for location of interest
    group_pop_var : string
        Variable containing the population count of the group of interest
    total_pop_var : string
        Variable in data that contains the total population count of the unit

    Returns
    ----------
    statistic : float
        Entropy index statistic value
    core_data : pandas.DataFrame
        A pandas DataFrame that contains the columns used to perform the estimate.

    Notes
    -----
    Based on Massey, Douglas S., and Nancy A. Denton. "The dimensions of residential segregation." Social forces 67.2 (1988): 281-315.

    Reference: :cite:`massey1988dimensions`.

    """
    x = np.array(data[group_pop_var])
    t = np.array(data[total_pop_var])

    if any(t < x):
        raise ValueError(
            "Group of interest population must equal or lower than the total population of the units."
        )

    T = t.sum()
    P = x.sum() / T

    # If a unit has zero population, the group of interest frequency is zero
    pi = np.where(t == 0, 0, x / t)

    E = P * np.log(1 / P) + (1 - P) * np.log(1 / (1 - P))
    Ei = pi * np.log(1 / pi) + (1 - pi) * np.log(1 / (1 - pi))
    Ei = np.nan_to_num(Ei)  # replace nan with 0
    H = np.nansum(
        t * (E - Ei) / (E * T)
    )  # If some pi is zero, numpy will treat as zero

    if not isinstance(data, gpd.GeoDataFrame):
        core_data = data[[group_pop_var, total_pop_var]]

    else:
        core_data = data[[group_pop_var, total_pop_var, data.geometry.name]]

    return H, core_data


class Entropy(SingleGroupIndex, SpatialImplicitIndex):
    """Entropy Index.

    Parameters
    ----------
    data : pandas.DataFrame or geopandas.GeoDataFrame, required
        dataframe or geodataframe if spatial index holding data for location of interest
    group_pop_var : str, required
        name of column on dataframe holding population totals for focal group
    total_pop_var : str, required
        name of column on dataframe holding total overall population
    w : libpysal.weights.KernelW, optional
        lipysal spatial kernel weights object used to define an egohood
    network : pandana.Network
        pandana Network object representing the study area
    distance : int
        Maximum distance (in units of geodataframe CRS) to consider the extent of the egohood
    decay : str
        type of decay function to apply. Options include
    precompute : bool
        Whether to precompute the pandana Network object

    Attributes
    ----------
    statistic : float
                Entropy Index
    core_data : a pandas DataFrame
                A pandas DataFrame that contains the columns used to perform the estimate.

    Notes
    -----
    Based on Massey, Douglas S., and Nancy A. Denton. "The dimensions of residential segregation." Social forces 67.2 (1988): 281-315.

    Reference: :cite:`massey1988dimensions`.
    """

    def __init__(
        self,
        data,
        group_pop_var,
        total_pop_var,
        w=None,
        network=None,
        distance=None,
        decay=None,
        function="triangular",
        precompute=None,
        **kwargs
    ):
        """Init."""

        SingleGroupIndex.__init__(self, data, group_pop_var, total_pop_var)
        if any([w, network, distance]):
            SpatialImplicitIndex.__init__(
                self, w, network, distance, decay, function, precompute
            )
        aux = _entropy(self.data, self.group_pop_var, self.total_pop_var)

        self.statistic = aux[0]
        self.data = aux[1]
        self._function = _entropy
