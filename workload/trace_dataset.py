import numpy as np

class TraceDataset:

    def __init__(self):
        self.X = None  # 输入: cpu, mem
        self.y_latency = None
        self.y_accuracy = None

    def generate_synthetic_trace(self):
        """
        构造模拟 trace 数据
        """

        cpu = np.array([1, 1, 2, 2, 4, 4, 8, 8])
        mem = np.array([512, 1024, 512, 1024, 512, 1024, 512, 1024])
        resolution = np.array([640 * 480, 1280 * 720, 640 * 480, 1280 * 720,
                               640 * 480, 1280 * 720, 640 * 480, 1280 * 720])

        # 结果使用函数模拟 需要替换为真实数据集
        # 延迟函数
        latency = (resolution / 1e5) / cpu + 60 / (mem / 512)
        # 准确率函数
        accuracy = 0.5 + 0.1 * np.log2(cpu) + 0.05 * np.log2(resolution / (640 * 480))

        self.X = np.column_stack((cpu, mem, resolution))
        self.y_latency = latency
        self.y_accuracy = accuracy
