from twilio.rest import Client
import random

# Your Twilio Account SID and Auth Token
account_sid = 'AC0e513d862d9e34b231f64423859f6097'
auth_token = '446cb09b47202e035673914ffa202e7d'
client = Client(account_sid, auth_token)

# The phone number you want to send the OTP to (must be verified with Twilio)
to_phone_number = '+919892347706'

# Generate your OTP (you'll need to implement this logic)


otp=random.randint(0, 9999)
    

# Send the OTP via SMS
message = client.messages.create(
    body=f'Your OTP is: {otp}',
    from_='+16515381567',  # This is a Twilio phone number
    to=to_phone_number
)

print(message.sid)

# import requests
# resp = requests.post('https://textbelt.com/text', {
#   'phone': '+918928807754',
#   'message': 'Hello world',
#   'key': 'textbelt',
# })
# print(resp.json())