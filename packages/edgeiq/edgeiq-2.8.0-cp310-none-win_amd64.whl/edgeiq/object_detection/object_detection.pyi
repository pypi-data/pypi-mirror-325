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
from typing import TypeVar

SUPPORTED_ENGINES: Incomplete

class ObjectDetection(BaseService[ObjectDetectionProcessor, ObjectDetectionResults]):
    def __init__(self, model_id: str, model_config: ModelConfig | None = None, pre_process: PreProcessT | None = None, pre_process_batch: PreProcessBatchT | None = None, post_process: PostProcessT | None = None, post_process_batch: PostProcessBatchT | None = None) -> None: ...
    def detect_objects(self, image: np.ndarray, confidence_level: float = 0.3, overlap_threshold: float = 0.3) -> ObjectDetectionResults: ...
    def detect_objects_batch(self, images: list[np.ndarray], confidence_level: float = 0.3, overlap_threshold: float = 0.3) -> list[ObjectDetectionResults]: ...

def markup_image(image: np.ndarray, predictions: list[ObjectDetectionPrediction], show_labels: bool = True, show_confidences: bool = True, colors: list[tuple[int, int, int]] | None = None, line_thickness: int = 2, font_size: float = 0.5, font_thickness: int = 2, text_box_padding: int = 10, bounding_box_corner_radius: int = 0, text_box_corner_radius: int = 0, text_box_alignment: TextAlignment = ('left', 'top'), text_box_position: TextAlignment | tuple[int, int] = ('left', 'top')) -> np.ndarray: ...
def overlay_transparent_boxes(image: np.ndarray, predictions: list[ObjectDetectionPrediction], alpha: float = 0.5, colors: list[tuple[int, int, int]] | None = None, show_labels: bool = False, show_confidences: bool = False): ...
def blur_objects(image: np.ndarray, predictions: list[ObjectDetectionPrediction]) -> np.ndarray: ...
PredictionT = TypeVar('PredictionT', bound=ObjectDetectionPrediction)

def filter_predictions_by_label(predictions: list[PredictionT], label_list: list[str]) -> list[PredictionT]: ...
def filter_predictions_by_area(predictions: list[PredictionT], min_area_thresh: float) -> list[PredictionT]: ...
