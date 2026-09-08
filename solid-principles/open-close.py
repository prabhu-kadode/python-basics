from abc import ABC,abstractmethod
class Notification:
    @abstractmethod
    def send(self,message):
        pass
class Email(Notification):
    def send(self,message):
        print("Email being sent")
class SMS(Notification):
    def send(self,message):
        print("SMS service is being sent")

class Whatsapp(Notification):
    def send(self,message):
        print("SMS service is being sent")

class User:
    def __init__(self,notification):
        self.notification = notification
    def create_user(self):
        print("User created")
        self.notification.send("hi hello")

# email = Email()
sms = SMS()

user = User(sms)
user.create_user()