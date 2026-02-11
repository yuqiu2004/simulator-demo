class Hook:
    def before_event(self, event, engine):
        pass

    def after_event(self, event, engine):
        pass


class HookManager:
    def __init__(self):
        self._hooks = []

    def register(self, hook):
        self._hooks.append(hook)

    def execute(self, phase, event, engine):
        for hook in self._hooks:
            method = getattr(hook, phase, None)
            if method:
                method(event, engine)
