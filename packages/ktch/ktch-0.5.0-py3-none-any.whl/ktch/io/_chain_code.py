"""Chain-code file I/O functions"""

# Copyright 2024 Koji Noshita
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass

import numpy as np


@dataclass
class ChainCodeData:
    """Chain-code data structure

    Parameters
    ==========
    idx: str
        index of the chain-code
    chc: list of int
        chain-code
    scale: float
        scale factor
    """

    idx: str
    chc: list
    scale: float
    desc: dict = None

    @property
    def idx(self) -> str:
        return self._idx

    @idx.setter
    def idx(self, idx: str):
        self._idx = idx

    @property
    def chc(self) -> list:
        return self._chc

    @chc.setter
    def chc(self, chc: list):
        self._chc = chc

    @property
    def scale(self) -> float:
        return self._scale

    @scale.setter
    def scale(self, scale: float):
        self._scale = scale


def read_chc(file_path):
    """Read chain-code from a file

    Parameters
    ==========
    file_path: str
        path to the chain-code file (.chc)

    Returns
    =======
    x: Coordinate values converted from chain-code
    """
    with open(file_path, "r") as f:
        chc = f.readlines()

    return x


def _chain_code_to_coordinate(chc):
    """Convert chain-code to coordinate values

    Parameters
    ==========
    chc: list of str
        chain-code

    Returns
    =======
    x: list of tuple
        coordinate values
    """

    _chain_code_to_displacement = {
        0: np.array([1, 0]),
        1: np.array([1, 1]),
        2: np.array([0, 1]),
        3: np.array([-1, 1]),
        4: np.array([-1, 0]),
        5: np.array([-1, -1]),
        6: np.array([0, -1]),
        7: np.array([1, -1]),
    }

    x = [np.array([0, 0])]
    for c in chc:
        dx = _chain_code_to_displacement[c]
        x.append(x[-1] + dx)

    x = np.array(x)

    return x
