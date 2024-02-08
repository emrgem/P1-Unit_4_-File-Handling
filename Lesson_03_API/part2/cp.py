from twilio.rest import Client

account_sid = 'AC82ab96ca53c90d4a9ee731e8b527068a'
auth_token = '34ccdc36f15eaf47532e9da772a41094'
client = Client(account_sid, auth_token)
twilio_phone = '+18447223757'

# Recipient phone number
recipient_phone = '+18777804236'
#Create a twilio client
client = Client(account_sid,auth_token)

#send an sms
def send_sms(message_body):
    message = client.messages.create(
        body = message_body,
        from_= twilio_phone,
        to = recipient_phone
    )
    print(f"Message sent with SID:{message.sid}")
message_body = "Hello from BT!"
send_sms(message_body)