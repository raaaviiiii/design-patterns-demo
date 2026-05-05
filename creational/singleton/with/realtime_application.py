import threading
import time


class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()  # ensures thread safety

    def __new__(cls, *args, **kwargs):
        # Double-checked locking
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    print("[DB] Creating new database connection...")
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self, dsn: str):
        # Prevent re-initialization
        if self._initialized:
            return

        self.dsn = dsn
        self.connected = False
        self._connect()
        self._initialized = True

    def _connect(self):
        print(f"[DB] Connecting to {self.dsn} ...")
        time.sleep(1)  # simulate I/O
        self.connected = True
        print("[DB] Connection established")

    def query(self, sql: str):
        if not self.connected:
            raise RuntimeError("Not connected to DB")
        print(f"[DB] Executing: {sql}")
        return {"rows": [], "count": 0}


# 🔹 Client / App Layer
if __name__ == "__main__":
    # Simulate multiple parts of an app asking for DB
    db1 = DatabaseConnection("postgresql://user:pass@localhost:5432/appdb")
    db2 = DatabaseConnection("postgresql://user:pass@localhost:5432/appdb")

    print("Same instance?", db1 is db2)

    db1.query("SELECT * FROM users")