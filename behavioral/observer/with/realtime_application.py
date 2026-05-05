from abc import ABC, abstractmethod
from typing import List


# 🔹 Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, event_data):
        pass


# 🔹 Concrete Observers (Subscribers)

class EmailNotifier(Observer):
    def update(self, event_data):
        print(f"[Email] Sending email: {event_data}")


class SMSNotifier(Observer):
    def update(self, event_data):
        print(f"[SMS] Sending SMS: {event_data}")


class PushNotifier(Observer):
    def update(self, event_data):
        print(f"[Push] Sending push notification: {event_data}")


# 🔹 Subject (Publisher)

class EventManager:
    def __init__(self):
        self.subscribers: List[Observer] = []

    def subscribe(self, observer: Observer):
        print(f"[EventManager] Subscribed: {observer.__class__.__name__}")
        self.subscribers.append(observer)

    def unsubscribe(self, observer: Observer):
        self.subscribers.remove(observer)

    def notify(self, event_data):
        print("\n[EventManager] Notifying subscribers...\n")
        for subscriber in self.subscribers:
            subscriber.update(event_data)


# 🔹 Real System Example → YouTube Channel

class YouTubeChannel:
    def __init__(self, name):
        self.name = name
        self.event_manager = EventManager()

    def subscribe(self, observer):
        self.event_manager.subscribe(observer)

    def upload_video(self, title):
        print(f"\n[YouTube] {self.name} uploaded: {title}")
        self.event_manager.notify(f"New video: {title}")


# 🔹 Client Code

if __name__ == "__main__":
    # Create channel
    channel = YouTubeChannel("TechWorld")

    # Create subscribers
    email = EmailNotifier()
    sms = SMSNotifier()
    push = PushNotifier()

    # Subscribe
    channel.subscribe(email)
    channel.subscribe(sms)
    channel.subscribe(push)

    # Trigger event
    channel.upload_video("Design Patterns Explained")