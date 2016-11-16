from twilio import rest

account_sid = "AC258580f92cd61759fdeaf716399be1fd" # Your Account SID from www.twilio.com/console
auth_token  = "dbd80195f79534c84c5fe8b2af817526"  # Your Auth Token from www.twilio.com/console

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Python twilio",
    to="+16138903990",    # Replace with your phone number
    from_="+13437005738") # Replace with your Twilio number

print(message.sid)
