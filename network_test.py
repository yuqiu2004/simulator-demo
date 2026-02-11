from network.config import NetworkConfig
from network.topology import Topology
from network.engine import SimulationEngine
from network.network_layer import NetworkLayer
from network.packet import Packet
from network.hook import HookManager
from network.disturbances import LinkFailureHook


config_data = {
    "nodes": [
        {"id": "cloud1", "type": "cloud"},
        {"id": "edge1", "type": "edge"},
        {"id": "device1", "type": "device"}
    ],
    "links": [
        {"src": "cloud1", "dst": "edge1", "bandwidth": 100, "delay": 10},
        {"src": "edge1", "dst": "device1", "bandwidth": 50, "delay": 5}
    ]
}

# 构建网络
config = NetworkConfig(config_data)
topology = Topology()
topology.build_from_config(config)

engine = SimulationEngine()
network = NetworkLayer(topology, engine)

engine.network = network
engine.hooks = HookManager()

# 注册扰动
engine.hooks.register(LinkFailureHook(8, ("edge1", "device1")))

# 发送数据
packet = Packet("cloud1", "device1", 100)
network.send_packet(packet)

# 运行
engine.run(until=50)
