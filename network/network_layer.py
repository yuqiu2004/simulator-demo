from .event import Event

class NetworkLayer:
    def __init__(self, topology, engine):
        self.topology = topology
        self.engine = engine

    def send_packet(self, packet):
        path = self.topology.shortest_path(packet.src, packet.dst)
        packet.path = path

        total_delay = 0
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]

            if self.topology.get_link_attr(u, v, "status") == "DOWN":
                print(f"Link {u}-{v} is DOWN")
                return

            delay = self.topology.get_link_attr(u, v, "delay")
            total_delay += delay

        event = Event(
            time=self.engine.current_time + total_delay,
            event_type="PACKET_SEND",
            payload={"packet": packet}
        )

        self.engine.schedule(event)

    def _handle_packet(self, event):
        packet = event.payload["packet"]
        print(f"[{self.engine.current_time}] Packet arrived at {packet.dst}")
