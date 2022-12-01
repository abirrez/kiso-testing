##########################################################################
# Copyright (c) 2010-2022 Robert Bosch GmbH
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0.
#
# SPDX-License-Identifier: EPL-2.0
##########################################################################

"""
Define some recurring typing definitions
"""

from __future__ import annotations

import pathlib
import typing
from typing import Dict, Union

from . import message

PathType = Union[str, pathlib.Path]
MsgType = Union[message.Message, bytes, str]
ProxyReturn = Dict[str, Union[bytes, int, message.Message, None]]