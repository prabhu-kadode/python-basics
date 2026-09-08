class User:
    def __init__(self,email):
        print("hi hello")
        self.email = email
    def create_user(self):
        print("user created")
        self.email.send_mail("id")
class Email:
    def __init__(self):
        pass
    def send_mail(self,id):
        print("Sending mail..")

email = Email()
user = User(email)
user.create_user()
