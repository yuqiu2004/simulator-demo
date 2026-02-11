class Packet:
    def __init__(self, src, dst, size):
        self.src = src
        self.dst = dst
        self.size = size
        self.path = []
