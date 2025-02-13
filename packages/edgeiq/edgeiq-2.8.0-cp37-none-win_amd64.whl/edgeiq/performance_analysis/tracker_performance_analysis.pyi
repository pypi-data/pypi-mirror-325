import numpy as np
from _typeshed import Incomplete
from edgeiq import ObjectDetectionPrediction as ObjectDetectionPrediction, TrackablePrediction as TrackablePrediction
from typing import Dict, List, Tuple

TrackingResults: Incomplete

class ObjectData:
    tracked_ids: List[int]
    num_id_changes: int
    def __init__(self, tracked_ids, num_id_changes) -> None: ...

class IdChangeEvent:
    ground_truth_id: int
    last_tracker_id: int
    new_tracker_id: int
    def __init__(self, ground_truth_id, last_tracker_id, new_tracker_id) -> None: ...

class IdSwapEvent:
    last_ground_truth_id: int
    new_ground_truth_id: int
    def __init__(self, last_ground_truth_id, new_ground_truth_id) -> None: ...

class IdChangeReport:
    num_objects_with_id_changes: int
    objects_with_id_changes: List[int]
    total_id_changes: int
    id_change_events_by_frame: Dict[int, List[IdChangeEvent]]
    id_changes_by_ground_truth_id: Dict[int, ObjectData]
    def write_to_file(self, output_dir: str): ...
    def __init__(self, num_objects_with_id_changes, objects_with_id_changes, total_id_changes, id_change_events_by_frame, id_changes_by_ground_truth_id) -> None: ...

class IdSwapReport:
    num_objects_with_id_swaps: int
    id_swaps_by_ground_truth_id: Dict[int, List[int]]
    total_object_swaps: int
    id_swap_events_by_frame: Dict[int, List[IdSwapEvent]]
    def write_to_file(self, output_dir: str): ...
    def __init__(self, num_objects_with_id_swaps, id_swaps_by_ground_truth_id, total_object_swaps, id_swap_events_by_frame) -> None: ...

class TrackerPerformanceAnalyzer:
    def __init__(self, ground_truth: List[TrackingResults], max_distance: int) -> None: ...
    def update(self, frame_idx: int, results: TrackingResults): ...
    def markup_image(self, frame_idx: int, frame: np.ndarray, color: Tuple[int, int, int]) -> np.ndarray: ...
    def generate_report(self) -> Tuple[IdChangeReport, IdSwapReport]: ...
