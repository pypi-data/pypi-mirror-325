from .trackable_prediction import TrackablePrediction as TrackablePrediction
from .tracker_algorithm import TrackerAlgorithm as TrackerAlgorithm
from .tracking_results import TrackingResults as TrackingResults
from edgeiq._constants import SupportedPurposes as SupportedPurposes
from edgeiq.exceptions import NoMoreResults as NoMoreResults
from edgeiq.object_detection import ObjectDetectionPrediction as ObjectDetectionPrediction
from typing import Sequence

class TrackerAnalytics(TrackerAlgorithm[TrackablePrediction[ObjectDetectionPrediction], ObjectDetectionPrediction]):
    def __init__(self, annotations: list[TrackingResults]) -> None: ...
    def update(self, predictions: Sequence[ObjectDetectionPrediction], **trackable_kwargs) -> TrackingResults[TrackablePrediction]: ...
