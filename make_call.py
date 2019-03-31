from twilio.rest import Client
from credentials import user_id,password


account_sid=user_id
auth_token=password

client=Client(account_sid,auth_token)

call = client.calls.create(
                        from_="your no",
                        to="receiver",
                        url="http://demo.twilio.com/docs/voice.xml"
                    )

print(call.sid)