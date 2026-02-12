from .load_query import LoadQuery
from .execution_result import ExecutionResult

class ExecutionModel:

    def __init__(self):
        pass

    def execute(self, query: LoadQuery) -> ExecutionResult:
        """
        留空：后续实现真实帧采集与执行
        """
        raise NotImplementedError("Execution-driven mode not implemented yet.")
