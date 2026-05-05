from abc import ABC, abstractmethod
import time


# 🔹 Component Interface
class RequestHandler(ABC):
    @abstractmethod
    def handle(self, request):
        pass


# 🔹 Concrete Component (Core logic)
class BasicHandler(RequestHandler):
    def handle(self, request):
        print(f"[Handler] Processing request: {request}")


# 🔹 Base Decorator
class HandlerDecorator(RequestHandler):
    def __init__(self, handler: RequestHandler):
        self.handler = handler

    def handle(self, request):
        self.handler.handle(request)


# 🔹 Concrete Decorators

class LoggingDecorator(HandlerDecorator):
    def handle(self, request):
        print("[Logging] Request received")
        self.handler.handle(request)
        print("[Logging] Request completed")


class AuthDecorator(HandlerDecorator):
    def handle(self, request):
        if not request.get("authenticated", False):
            print("[Auth] Unauthorized request")
            return
        print("[Auth] User authenticated")
        self.handler.handle(request)


class TimingDecorator(HandlerDecorator):
    def handle(self, request):
        start = time.time()
        self.handler.handle(request)
        end = time.time()
        print(f"[Timing] Took {end - start:.4f} seconds")


# 🔹 Client Code
if __name__ == "__main__":
    request = {"user": "Ravi", "authenticated": True}

    # Wrap decorators dynamically
    handler = BasicHandler()
    handler = LoggingDecorator(handler)
    handler = AuthDecorator(handler)
    handler = TimingDecorator(handler)

    handler.handle(request)