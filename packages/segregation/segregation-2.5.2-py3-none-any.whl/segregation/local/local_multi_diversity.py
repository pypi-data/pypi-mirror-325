"""Multigroup dissimilarity index"""

__author__ = "Renan X. Cortes <renanc@ucr.edu>, Sergio J. Rey <sergio.rey@ucr.edu> and Elijah Knaap <elijah.knaap@ucr.edu>"

import numpy as np

from .._base import MultiGroupIndex, SpatialImplicitIndex

np.seterr(divide="ignore", invalid="ignore")


def _multi_local_diversity(data, groups):
    """
    Calculation of Local Diversity index for each group and unit

    Parameters
    ----------

    data   : a pandas DataFrame of n rows
    groups : list of strings of length k.
             The variables names in data of the groups of interest of the analysis.

    Returns
    -------

    statistics : np.array(n,k)
                 Local Diversity values for each group and unit

    core_data  : a pandas DataFrame
                 A pandas DataFrame that contains the columns used to perform the estimate.

    Notes
    -----
    Based on Theil, Henry. Statistical decomposition analysis; with applications in the social and administrative sciences. No. 04; HA33, T4.. 1972.

    Reference: :cite:`theil1972statistical`.

    """

    core_data = data[groups]

    df = np.array(core_data)

    ti = df.sum(axis=1)
    pik = df / ti[:, None]

    multi_LD = -np.nansum(pik * np.log(pik), axis=1)

    return multi_LD, core_data, groups


class MultiLocalDiversity(MultiGroupIndex, SpatialImplicitIndex):
    """Multigroup Local Diversity Index.

    Parameters
    ----------
    data : pandas.DataFrame or geopandas.GeoDataFrame, required
        dataframe or geodataframe if spatial index holding data for location of interest
    groups : list, required
        list of columns on dataframe holding population totals for each group
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
        Multigroup Dissimilarity Index value
    core_data : a pandas DataFrame
        DataFrame that contains the columns used to perform the estimate.
    """

    def __init__(
        self,
        data,
        groups,
        w=None,
        network=None,
        distance=None,
        decay=None,
        precompute=None,
        function="triangular",
    ):
        """Init."""

        MultiGroupIndex.__init__(self, data, groups)
        if any([w, network, distance]):
            SpatialImplicitIndex.__init__(
                self, w, network, distance, decay, function, precompute
            )
        aux = _multi_local_diversity(self.data, self.groups)

        self.statistics = aux[0]
        self.data = aux[1]
        self.groups = aux[2]
        self._function = _multi_local_diversity
