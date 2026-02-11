from .event import EventQueue

class SimulationEngine:
    def __init__(self):
        self.current_time = 0
        self.event_queue = EventQueue()
        self.hooks = None
        self.network = None

    def schedule(self, event):
        self.event_queue.push(event)

    def run(self, until=float("inf")):
        while not self.event_queue.empty():
            event = self.event_queue.pop()

            if event.time > until:
                break

            self.current_time = event.time

            if self.hooks:
                self.hooks.execute("before_event", event, self)

            self.dispatch(event)

            if self.hooks:
                self.hooks.execute("after_event", event, self)

    def dispatch(self, event):
        if event.event_type == "PACKET_SEND":
            self.network._handle_packet(event)
