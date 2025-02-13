import numpy as np
from _typeshed import Incomplete
from enum import Enum

class MOG2:
    cuda: Incomplete
    history: Incomplete
    var_threshold: Incomplete
    detect_shadows: Incomplete
    bgmog2: Incomplete
    def __init__(self, history: int = 120, var_threshold: float = 250.0, detect_shadows: bool = True, cuda: bool = False) -> None: ...
    frame: Incomplete
    def process_frame(self, frame: np.ndarray, learning_rate: float = -1.0): ...

def get_contours(raw_contours: list[np.ndarray]): ...
def get_boundingboxes(contours: list[np.ndarray]): ...
def get_moments(contours: list[np.ndarray]): ...

class SortingMethod(Enum):
    LEFT_RIGHT = 'left-to-right'
    RIGHT_LEFT = 'right-to-left'
    BOTTOM_TOP = 'bottom-to-top'
    TOP_BOTTOM = 'top-to-bottom'

def get_sorted(method: SortingMethod, contours: list[np.ndarray]): ...
