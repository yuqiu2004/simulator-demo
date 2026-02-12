from workload.load_layer import LoadLayer
from workload.load_query import LoadQuery
from workload.resource_quota import ResourceQuota

load_layer = LoadLayer(mode="trace")

# 模拟一帧的效果
query = LoadQuery(
    timestamp=10.5,
    frame_id=150,
    resolution=480*480,
    resource=ResourceQuota(cpu_cores=4, memory_mb=1024)
)

result = load_layer.query(query)

print("Latency:", result.latency)
print("Detection Rate:", result.detection_rate)
print("Accuracy:", result.accuracy)
