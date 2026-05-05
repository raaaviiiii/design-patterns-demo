class Subscriber:
    def update(self):
        print("Got notification")

class YouTube:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, sub):
        self.subscribers.append(sub)

    def notify(self):
        for s in self.subscribers:
            s.update()

if __name__ == "__main__":
    yt = YouTube()
    s1 = Subscriber()
    yt.subscribe(s1)
    yt.notify()