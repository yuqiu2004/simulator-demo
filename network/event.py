import heapq

class Event:
    def __init__(self, time, event_type, payload=None):
        self.time = time
        self.event_type = event_type
        self.payload = payload or {}

    def __lt__(self, other):
        return self.time < other.time


class EventQueue:
    def __init__(self):
        self._queue = []

    def push(self, event):
        heapq.heappush(self._queue, event)

    def pop(self):
        return heapq.heappop(self._queue)

    def empty(self):
        return len(self._queue) == 0
