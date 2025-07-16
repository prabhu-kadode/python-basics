class Validation:
    def __init__(self,email):
        self.email = email
    def isValidaMail(self):
        email = self.email
        
        
class SendMail:
    def __init__(self):
        self._to= None
        self._subject= None
        self._from= None
        self._message = None
        
    def toEmail(self,email):
        self._to = email
        return self
    def fromEmail(self,email):
        self._from = email
        return self
    def subject(self,sub):
        self._subject = sub
        return self
    def message(self,msg):
        self._message = msg
        return self
    def sendMail(self):
        print('Sending  mail...')
        print('sent')
        return True
emailSent = (SendMail()
             .toEmail('sppsps')
             .fromEmail('sss')
             .subject('hi')
             .message("how are you")
             .sendMail())
print(emailSent)

    


