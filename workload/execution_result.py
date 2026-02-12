class ExecutionResult:
    def __init__(self, latency: float, detection_rate: float, accuracy: float):
        self.latency = latency
        self.detection_rate = detection_rate
        self.accuracy = accuracy

    def __repr__(self):
        return f"ExecutionResult(latency={self.latency}, detection_rate={self.detection_rate}, accuracy={self.accuracy})"

    def __eq__(self, other):
        if not isinstance(other, ExecutionResult):
            return NotImplemented
        return (self.latency == other.latency and
                self.detection_rate == other.detection_rate and
                self.accuracy == other.accuracy)