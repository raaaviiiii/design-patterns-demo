from abc import ABC, abstractmethod
from queue import Queue
import time


# 🔹 Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# 🔹 Receiver Classes (Actual business logic)

class EmailService:
    def send_email(self, to, message):
        print(f"[EmailService] Sending email to {to}: {message}")
        time.sleep(1)
        print("[EmailService] Email sent")


class PaymentService:
    def process_payment(self, user, amount):
        print(f"[PaymentService] Processing ₹{amount} payment for {user}")
        time.sleep(1)
        print("[PaymentService] Payment successful")


class ReportService:
    def generate_report(self):
        print("[ReportService] Generating report...")
        time.sleep(1)
        print("[ReportService] Report ready")


# 🔹 Concrete Commands

class SendEmailCommand(Command):
    def __init__(self, email_service, to, message):
        self.email_service = email_service
        self.to = to
        self.message = message

    def execute(self):
        self.email_service.send_email(self.to, self.message)


class ProcessPaymentCommand(Command):
    def __init__(self, payment_service, user, amount):
        self.payment_service = payment_service
        self.user = user
        self.amount = amount

    def execute(self):
        self.payment_service.process_payment(self.user, self.amount)


class GenerateReportCommand(Command):
    def __init__(self, report_service):
        self.report_service = report_service

    def execute(self):
        self.report_service.generate_report()


# 🔹 Invoker (Task Queue System)

class TaskQueue:
    def __init__(self):
        self.queue = Queue()

    def add_task(self, command: Command):
        print(f"[TaskQueue] Task added: {command.__class__.__name__}")
        self.queue.put(command)

    def process_tasks(self):
        print("\n[TaskQueue] Processing tasks...\n")
        while not self.queue.empty():
            command = self.queue.get()
            command.execute()


# 🔹 Client Code (Application Layer)

if __name__ == "__main__":
    # Services
    email_service = EmailService()
    payment_service = PaymentService()
    report_service = ReportService()

    # Commands
    email_cmd = SendEmailCommand(email_service, "user@gmail.com", "Welcome!")
    payment_cmd = ProcessPaymentCommand(payment_service, "Ravi", 5000)
    report_cmd = GenerateReportCommand(report_service)

    # Task Queue (Invoker)
    queue = TaskQueue()

    # Add tasks
    queue.add_task(email_cmd)
    queue.add_task(payment_cmd)
    queue.add_task(report_cmd)

    # Process tasks
    queue.process_tasks()