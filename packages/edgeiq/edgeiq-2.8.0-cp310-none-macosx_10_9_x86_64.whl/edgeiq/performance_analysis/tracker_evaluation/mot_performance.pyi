from . import datasets as datasets, metrics as metrics, utils as utils
from .metrics import Count as Count
from _typeshed import Incomplete
from edgeiq.performance_analysis.tracker_evaluation.metrics._base_metric import _BaseMetric

class _MOTEvaluator:
    def __init__(self, seq: str, gt_pth: str, tracker_pth: str, metrics_list: list[_BaseMetric], metric_names: list[str]) -> None: ...
    def evaluate(self): ...

class MOTEvaluator:
    gt_files: Incomplete
    tracker_files: Incomplete
    metrics_list: Incomplete
    output_path: Incomplete
    def __init__(self, gt_files: list[str], tracker_files: list[str], metrics_list: list[str], output_pth: str | None = None, **kwargs) -> None: ...
    def evaluate_all(self) -> None: ...
