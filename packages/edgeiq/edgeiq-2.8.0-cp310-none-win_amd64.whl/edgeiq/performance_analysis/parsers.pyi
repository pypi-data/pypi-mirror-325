from _typeshed import Incomplete
from edgeiq import Dict as Dict, ObjectDetectionResults as ObjectDetectionResults
from edgeiq.bounding_box import BoundingBox as BoundingBox
from edgeiq.object_detection import ObjectDetectionPrediction as ObjectDetectionPrediction

TrackablePrediction: Incomplete
TrackingResults: Incomplete

def parse_cvat_annotations(path: str, start_frame: int = 0, end_frame: int | None = None, new_id_for_occlusion: bool = False) -> tuple[Dict[int, ObjectDetectionPrediction], Dict[int, Dict[str, list[int]]]]: ...
def parse_coco_annotations(path: str) -> list[ObjectDetectionResults]: ...
def parse_mot_annotations(path: str, labels: list[str]) -> list[TrackingResults]: ...
