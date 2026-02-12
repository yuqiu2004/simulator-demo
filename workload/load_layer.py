from .trace_model import TraceModel
from .trace_dataset import TraceDataset
from .execution_model import ExecutionModel
from .load_query import LoadQuery
from .execution_result import ExecutionResult

class LoadLayer:

    def __init__(self, mode="trace"):

        self.mode = mode

        if mode == "trace":
            dataset = TraceDataset()
            dataset.generate_synthetic_trace()

            self.model = TraceModel(degree=3)
            self.model.fit(dataset)

        elif mode == "execution":
            self.model = ExecutionModel()

        else:
            raise ValueError("Unknown mode")

    def query(self, query: LoadQuery) -> ExecutionResult:

        if self.mode == "trace":
            return self.model.predict(query)

        elif self.mode == "execution":
            return self.model.execute(query)
