import numpy as np
from _typeshed import Incomplete
from dataclasses import dataclass
from edgeiq import ObjectDetectionPrediction as ObjectDetectionPrediction, TrackablePrediction as TrackablePrediction

TrackingResults: Incomplete

@dataclass
class ObjectData:
    tracked_ids: list[int] = ...
    num_id_changes: int = ...
    def __init__(self, tracked_ids=..., num_id_changes=...) -> None: ...

@dataclass
class IdChangeEvent:
    ground_truth_id: int
    last_tracker_id: int
    new_tracker_id: int
    def __init__(self, ground_truth_id, last_tracker_id, new_tracker_id) -> None: ...

@dataclass
class IdSwapEvent:
    last_ground_truth_id: int
    new_ground_truth_id: int
    def __init__(self, last_ground_truth_id, new_ground_truth_id) -> None: ...

@dataclass
class IdChangeReport:
    num_objects_with_id_changes: int
    objects_with_id_changes: list[int]
    total_id_changes: int
    id_change_events_by_frame: dict[int, list[IdChangeEvent]]
    id_changes_by_ground_truth_id: dict[int, ObjectData]
    def write_to_file(self, output_dir: str): ...
    def __init__(self, num_objects_with_id_changes, objects_with_id_changes, total_id_changes, id_change_events_by_frame, id_changes_by_ground_truth_id) -> None: ...

@dataclass
class IdSwapReport:
    num_objects_with_id_swaps: int
    id_swaps_by_ground_truth_id: dict[int, list[int]]
    total_object_swaps: int
    id_swap_events_by_frame: dict[int, list[IdSwapEvent]]
    def write_to_file(self, output_dir: str): ...
    def __init__(self, num_objects_with_id_swaps, id_swaps_by_ground_truth_id, total_object_swaps, id_swap_events_by_frame) -> None: ...

class TrackerPerformanceAnalyzer:
    def __init__(self, ground_truth: list[TrackingResults], max_distance: int) -> None: ...
    def update(self, frame_idx: int, results: TrackingResults): ...
    def markup_image(self, frame_idx: int, frame: np.ndarray, color: tuple[int, int, int]) -> np.ndarray: ...
    def generate_report(self) -> tuple[IdChangeReport, IdSwapReport]: ...
