from . import datasets as datasets, metrics as metrics, utils as utils
from .metrics import Count as Count
from _typeshed import Incomplete
from edgeiq.performance_analysis.tracker_evaluation.metrics._base_metric import _BaseMetric
from typing import List, Optional

class _MOTEvaluator:
    def __init__(self, seq: str, gt_pth: str, tracker_pth: str, metrics_list: List[_BaseMetric], metric_names: List[str]) -> None: ...
    def evaluate(self): ...

class MOTEvaluator:
    gt_files: Incomplete
    tracker_files: Incomplete
    metrics_list: Incomplete
    output_path: Incomplete
    def __init__(self, gt_files: List[str], tracker_files: List[str], metrics_list: List[str], output_pth: Optional[str] = ..., **kwargs) -> None: ...
    def evaluate_all(self) -> None: ...
