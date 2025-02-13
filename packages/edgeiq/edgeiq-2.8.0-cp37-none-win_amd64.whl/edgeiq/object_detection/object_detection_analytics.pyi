import numpy as np
from .object_detection import ObjectDetectionResults as ObjectDetectionResults
from edgeiq._constants import SupportedPurposes as SupportedPurposes
from edgeiq.base_service import BaseService as BaseService
from edgeiq.exceptions import NoMoreResults as NoMoreResults
from edgeiq.model_config.model_config import ModelConfig as ModelConfig
from edgeiq.processing.object_detection.object_detection import ObjectDetectionProcessor as ObjectDetectionProcessor
from typing import List, Optional

class ObjectDetectionAnalytics(BaseService[ObjectDetectionProcessor, ObjectDetectionResults]):
    def __init__(self, annotations: List[List[ObjectDetectionResults]], model_id: str, model_config: Optional[ModelConfig] = ...) -> None: ...
    def detect_objects_for_stream(self, stream_idx: int, confidence_level: float = ..., overlap_threshold: float = ...) -> ObjectDetectionResults: ...
    def detect_objects(self, image: Optional[np.ndarray], confidence_level: float = ..., overlap_threshold: float = ...) -> ObjectDetectionResults: ...
    def detect_objects_batch(self, images: Optional[List[np.ndarray]], confidence_level: float = ..., overlap_threshold: float = ...) -> List[ObjectDetectionResults]: ...
