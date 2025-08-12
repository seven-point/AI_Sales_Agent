from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(to_number, message):
    return client.messages.create(
        body=message,
        from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
        to=f"whatsapp:{to_number}"
    )

def make_call(to_number, message_url):
    return client.calls.create(
        url=message_url,  # URL with TwiML or an MP3 to play
        to=to_number,
        from_=TWILIO_WHATSAPP_NUMBER
    )
