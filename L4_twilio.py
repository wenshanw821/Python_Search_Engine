from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "AC799d7a0825c71feda7f763653cf48eda"
# Your Auth Token from twilio.com/console
auth_token  = "8b27d50950bd6e9ded676beed9887e35"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+8615811056131",
    from_="+18572777404",
    body="Hello from Wenshan!")

print(message.sid)
