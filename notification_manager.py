from twilio.rest import Client

ACCOUNT_SID = ""
AUTH_TOKEN = ""
twilio_num = None
my_num = None


class NotificationManager:
    
    def __init__(self):
        self.client = Client(ACCOUNT_SID,AUTH_TOKEN)
    
    def send_message(self,message):
        message = self.client.messages.create(
            body=message,
            from_= twilio_num,
            to= my_num
        )
        print(message.sid)
