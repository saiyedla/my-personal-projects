from twilio.rest import Client

# Twilio credentials
account_sid = '<>'
auth_token = '<>'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Send a message
def send_whatsapp_message(to_number, message):
    try:
        message = client.messages.create(
            from_='whatsapp:<enter twilio number>,  
            body=message,
            to=f'whatsapp:{to_number}'      
        )
        print(f"Message sent successfully. SID: {message.sid}")
    except Exception as e:
        print(f"Error: {str(e)}")

recipient_number = 'RECIPIENT_WHATSAPP_NUMBER'
message_to_send = 'Hello'
send_whatsapp_message(recipient_number, message_to_send)
