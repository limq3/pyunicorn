#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This file is part of pyunicorn.
# Copyright (C) 2008--2018 Jonathan F. Donges and pyunicorn authors
# URL: <http://www.pik-potsdam.de/members/donges/software>
# License: BSD (3-clause)

"""
climate
=======

Provides classes for generating and analyzing complex climate networks.

Related Publications
~~~~~~~~~~~~~~~~~~~~
[Donges2009c]_, [Donges2009a]_, [Donges2009b]_, [Donges2011a]_, [Zou2011]_,
[Tominski2011]_, [Heitzig2012]_

To do
~~~~~
  - A lot - See current product backlog.

Known Bugs
~~~~~~~~~~
  - ...

"""

from ..core import GeoNetwork, Grid, Network

from .climate_data import ClimateData
from .climate_network import ClimateNetwork
from .coupled_climate_network import CoupledClimateNetwork
from .coupled_tsonis import CoupledTsonisClimateNetwork
from .havlin import HavlinClimateNetwork
from .hilbert import HilbertClimateNetwork
from .map_plots import MapPlots
from .mutual_info import MutualInfoClimateNetwork
from .partial_correlation import PartialCorrelationClimateNetwork
from .rainfall import RainfallClimateNetwork
from .spearman import SpearmanClimateNetwork
from .tsonis import TsonisClimateNetwork
from .eventsynchronization_climatenetwork import \
    EventSynchronizationClimateNetwork


#
#  Set global constants
#

#  Mean earth radius in kilometers
from ..core import EARTH_RADIUS
