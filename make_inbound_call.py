from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app= Flask(__name__)

@app.route("/voice",methods=['GET','POST'])
def voice():
    resp=VoiceResponse()

    resp.say("this failed also")

    return str(resp)

if __name__ == "__main__":
    app.run(port=139,debug=True)