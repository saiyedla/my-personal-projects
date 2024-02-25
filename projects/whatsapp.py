from twilio.rest import Client

# Twilio credentials
account_sid = 'AC0880156fb19602ea1cb359d41b1b5ab6'
auth_token = 'f2d80993aeb7f60eb1250c30f414b589'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Send a message
def send_whatsapp_message(to_number, message):
    try:
        message = client.messages.create(
            from_='+14155238886',  
            body=message,
            to=f'whatsapp:{to_number}'      
        )
        print(f"Message sent successfully. SID: {message.sid}")
    except Exception as e:
        print(f"Error: {str(e)}")

recipient_number = '+16137164686'
message_to_send = 'Hello'
send_whatsapp_message(+16137164686, message_to_send)
