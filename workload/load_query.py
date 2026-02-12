from .resource_quota import ResourceQuota

class LoadQuery:
    def __init__(self, timestamp: float, frame_id: int, resolution: int, resource: ResourceQuota):
        self.timestamp = timestamp
        self.frame_id = frame_id
        self.resolution = resolution
        self.resource = resource

    def __repr__(self):
        return f"LoadQuery(timestamp={self.timestamp}, frame_id={self.frame_id}, resource={self.resource})"

    def __eq__(self, other):
        if not isinstance(other, LoadQuery):
            return NotImplemented
        return (self.timestamp == other.timestamp and
                self.frame_id == other.frame_id and
                self.resource == other.resource)