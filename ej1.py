class EventManager:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event, callback):
        if event not in self.subscribers:
            self.subscribers[event] = []
        self.subscribers[event].append(callback)

    def unsubscribe(self, event, callback):
        if event in self.subscribers and callback in self.subscribers[event]:
            self.subscribers[event].remove(callback)

    def notify(self, event, data=None):
        if event in self.subscribers:
            for callback in self.subscribers[event]:
                callback(data)
