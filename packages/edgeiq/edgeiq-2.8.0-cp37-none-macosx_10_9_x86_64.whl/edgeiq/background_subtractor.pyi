import numpy as np
from _typeshed import Incomplete
from enum import Enum
from typing import List

class MOG2:
    cuda: Incomplete
    history: Incomplete
    var_threshold: Incomplete
    detect_shadows: Incomplete
    bgmog2: Incomplete
    def __init__(self, history: int = ..., var_threshold: float = ..., detect_shadows: bool = ..., cuda: bool = ...) -> None: ...
    frame: Incomplete
    def process_frame(self, frame: np.ndarray, learning_rate: float = ...): ...

def get_contours(raw_contours: List[np.ndarray]): ...
def get_boundingboxes(contours: List[np.ndarray]): ...
def get_moments(contours: List[np.ndarray]): ...

class SortingMethod(Enum):
    LEFT_RIGHT: str
    RIGHT_LEFT: str
    BOTTOM_TOP: str
    TOP_BOTTOM: str

def get_sorted(method: SortingMethod, contours: List[np.ndarray]): ...
