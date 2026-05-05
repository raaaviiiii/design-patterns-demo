class HttpRequest:
    def __init__(self):
        self.url = None
        self.method = None
        self.headers = {}
        self.params = {}
        self.body = None

    def send(self):
        print("\n[HTTP REQUEST]")
        print(f"Method: {self.method}")
        print(f"URL: {self.url}")
        print(f"Headers: {self.headers}")
        print(f"Params: {self.params}")
        print(f"Body: {self.body}")
        print("Request sent!\n")


# 🔹 Builder
class RequestBuilder:
    def __init__(self):
        self.request = HttpRequest()

    def set_url(self, url):
        self.request.url = url
        return self

    def set_method(self, method):
        self.request.method = method
        return self

    def add_header(self, key, value):
        self.request.headers[key] = value
        return self

    def add_param(self, key, value):
        self.request.params[key] = value
        return self

    def set_body(self, body):
        self.request.body = body
        return self

    def build(self):
        return self.request


# 🔹 Client Code
if __name__ == "__main__":
    request = (
        RequestBuilder()
        .set_url("https://api.example.com/users")
        .set_method("POST")
        .add_header("Authorization", "Bearer TOKEN")
        .add_header("Content-Type", "application/json")
        .add_param("page", 1)
        .set_body({"name": "Ravi", "role": "admin"})
        .build()
    )

    request.send()