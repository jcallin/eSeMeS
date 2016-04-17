from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
import os
from lib import directions

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def respond():
    ACCOUNT_SID = "ACe892e28b309a94844845c5f621ca451a"
    AUTH_TOKEN = "99426e30a3c5c2e25d5ba56f9087b7c3"
    OUR_NUMBER = "+18442306122"


    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    userMessage = request.values.get( 'Body', None )
    response = directions( userMessage )

    resp = twilio.twiml.Response()
    resp.message(response)
    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
