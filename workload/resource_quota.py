class ResourceQuota:
    def __init__(self, cpu_cores: int, memory_mb: int):
        self.cpu_cores = cpu_cores
        self.memory_mb = memory_mb

    def __repr__(self):
        return f"ResourceQuota(cpu_cores={self.cpu_cores}, memory_mb={self.memory_mb})"

    def __eq__(self, other):
        if not isinstance(other, ResourceQuota):
            return NotImplemented
        return (self.cpu_cores == other.cpu_cores and
                self.memory_mb == other.memory_mb)