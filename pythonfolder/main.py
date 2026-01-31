#============== EMAIL DATA BLUE PRINT====================
# This module defines classes for Email, User, and Inbox to simulate a simple email system.
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False

    def mark_as_read(self):
        self.read = True

class User:
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)

class Inbox:
    def __init__(self):
        self.emails = []

    def receive_email(self, email):
        self.emails.append(email)

alice = User("Alice")
bob = User("Bob")
recieve_email = Inbox()
print(alice.name)
alice.send_email(bob, "Geetings", "Hi Bob, how are you?")
for email in bob.inbox.emails:
    print(f"From: {email.sender.name}, Subject: {email.subject}, Body: {email.body} ")
