import networkx as nx

class Topology:
    def __init__(self):
        self.graph = nx.Graph()

    def build_from_config(self, config):
        for node in config.nodes:
            self.graph.add_node(node["id"], type=node["type"])

        for link in config.links:
            self.graph.add_edge(
                link["src"],
                link["dst"],
                bandwidth=link["bandwidth"],
                delay=link["delay"],
                status="UP"
            )

    def shortest_path(self, src, dst):
        return nx.shortest_path(self.graph, src, dst)

    def get_link_attr(self, u, v, key):
        return self.graph[u][v][key]

    def set_link_status(self, u, v, status):
        self.graph[u][v]["status"] = status
