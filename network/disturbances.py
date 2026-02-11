from .hook import Hook

class LinkFailureHook(Hook):
    def __init__(self, fail_time, link):
        self.fail_time = fail_time
        self.link = link
        self.failed = False

    def before_event(self, event, engine):
        if not self.failed and engine.current_time >= self.fail_time:
            u, v = self.link
            engine.network.topology.set_link_status(u, v, "DOWN")
            print(f"[{engine.current_time}] Link {u}-{v} FAILED")
            self.failed = True
