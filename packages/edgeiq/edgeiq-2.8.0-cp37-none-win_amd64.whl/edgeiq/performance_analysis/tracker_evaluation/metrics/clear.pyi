from .. import utils as utils
from ._base_metric import _BaseMetric
from _typeshed import Incomplete

class CLEAR(_BaseMetric):
    @staticmethod
    def get_default_config(): ...
    integer_fields: Incomplete
    float_fields: Incomplete
    fields: Incomplete
    summed_fields: Incomplete
    summary_fields: Incomplete
    config: Incomplete
    threshold: Incomplete
    def __init__(self, config: dict = ...) -> None: ...
    def eval_sequence(self, data: dict): ...
    def combine_sequences(self, all_res: dict): ...
