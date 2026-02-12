from .execution_result import ExecutionResult
from .load_query import LoadQuery
from .trace_dataset import TraceDataset
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np

class TraceModel:

    def __init__(self, degree=3):
        self.degree = degree
        self.poly = PolynomialFeatures(degree=self.degree)
        self.latency_model = LinearRegression()
        self.accuracy_model = LinearRegression()

    def fit(self, dataset: TraceDataset):

        X_poly = self.poly.fit_transform(dataset.X)

        self.latency_model.fit(X_poly, dataset.y_latency)
        self.accuracy_model.fit(X_poly, dataset.y_accuracy)

    def predict(self, query: LoadQuery):
        X = np.array([[query.resource.cpu_cores,
                       query.resource.memory_mb,
                       query.resolution]])
        X_poly = self.poly.transform(X)

        latency = self.latency_model.predict(X_poly)[0]
        accuracy = self.accuracy_model.predict(X_poly)[0]

        # detection_rate 可以由 accuracy 派生
        detection_rate = min(1.0, accuracy * 0.95)

        return ExecutionResult(
            latency=float(latency),
            detection_rate=float(detection_rate),
            accuracy=float(accuracy),
        )
