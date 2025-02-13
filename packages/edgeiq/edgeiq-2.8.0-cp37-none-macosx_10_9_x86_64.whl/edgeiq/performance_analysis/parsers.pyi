from _typeshed import Incomplete
from edgeiq import Dict as Dict, ObjectDetectionResults as ObjectDetectionResults
from edgeiq.bounding_box import BoundingBox as BoundingBox
from edgeiq.object_detection import ObjectDetectionPrediction as ObjectDetectionPrediction
from typing import List, Optional, Tuple

TrackablePrediction: Incomplete
TrackingResults: Incomplete

def parse_cvat_annotations(path: str, start_frame: int = ..., end_frame: Optional[int] = ..., new_id_for_occlusion: bool = ...) -> Tuple[Dict[int, ObjectDetectionPrediction], Dict[int, Dict[str, List[int]]]]: ...
def parse_coco_annotations(path: str) -> List[ObjectDetectionResults]: ...
def parse_mot_annotations(path: str, labels: List[str]) -> List[TrackingResults]: ...
