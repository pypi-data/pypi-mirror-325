import numpy as np
from .object_detection_prediction import ObjectDetectionPrediction as ObjectDetectionPrediction
from .object_detection_results import ObjectDetectionResults as ObjectDetectionResults
from _typeshed import Incomplete
from edgeiq._constants import SupportedPurposes as SupportedPurposes
from edgeiq.base_service import BaseService as BaseService
from edgeiq.bounding_box import BoundingBox as BoundingBox
from edgeiq.engine_accelerator import Engine as Engine
from edgeiq.model_config import ModelConfig as ModelConfig
from edgeiq.processing import ObjectDetectionProcessor as ObjectDetectionProcessor
from edgeiq.processing.object_detection.object_detection import PostProcessBatchT as PostProcessBatchT, PostProcessT as PostProcessT, PreProcessBatchT as PreProcessBatchT, PreProcessT as PreProcessT
from edgeiq.tools.image_manipulation import HorizontalTextAlignment as HorizontalTextAlignment, TextAlignment as TextAlignment, VerticalTextAlignment as VerticalTextAlignment, draw_rounded_rectangle as draw_rounded_rectangle, draw_text_with_background as draw_text_with_background
from typing import List, Optional, Tuple, TypeVar, Union

SUPPORTED_ENGINES: Incomplete

class ObjectDetection(BaseService[ObjectDetectionProcessor, ObjectDetectionResults]):
    def __init__(self, model_id: str, model_config: Optional[ModelConfig] = ..., pre_process: Optional[PreProcessT] = ..., pre_process_batch: Optional[PreProcessBatchT] = ..., post_process: Optional[PostProcessT] = ..., post_process_batch: Optional[PostProcessBatchT] = ...) -> None: ...
    def detect_objects(self, image: np.ndarray, confidence_level: float = ..., overlap_threshold: float = ...) -> ObjectDetectionResults: ...
    def detect_objects_batch(self, images: List[np.ndarray], confidence_level: float = ..., overlap_threshold: float = ...) -> List[ObjectDetectionResults]: ...

def markup_image(image: np.ndarray, predictions: List[ObjectDetectionPrediction], show_labels: bool = ..., show_confidences: bool = ..., colors: Optional[List[Tuple[int, int, int]]] = ..., line_thickness: int = ..., font_size: float = ..., font_thickness: int = ..., text_box_padding: int = ..., bounding_box_corner_radius: int = ..., text_box_corner_radius: int = ..., text_box_alignment: TextAlignment = ..., text_box_position: Union[TextAlignment, Tuple[int, int]] = ...) -> np.ndarray: ...
def overlay_transparent_boxes(image: np.ndarray, predictions: List[ObjectDetectionPrediction], alpha: float = ..., colors: Optional[List[Tuple[int, int, int]]] = ..., show_labels: bool = ..., show_confidences: bool = ...): ...
def blur_objects(image: np.ndarray, predictions: List[ObjectDetectionPrediction]) -> np.ndarray: ...
PredictionT = TypeVar('PredictionT', bound=ObjectDetectionPrediction)

def filter_predictions_by_label(predictions: List[PredictionT], label_list: List[str]) -> List[PredictionT]: ...
def filter_predictions_by_area(predictions: List[PredictionT], min_area_thresh: float) -> List[PredictionT]: ...
