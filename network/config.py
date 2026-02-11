class NetworkConfig:
    def __init__(self, config_dict):
        self.nodes = config_dict.get("nodes", [])
        self.links = config_dict.get("links", [])
