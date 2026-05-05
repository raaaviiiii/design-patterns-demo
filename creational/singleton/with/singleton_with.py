class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating Singleton Logger")
            cls._instance = super().__new__(cls)
        return cls._instance

if __name__ == "__main__":
    a = Logger()
    b = Logger()