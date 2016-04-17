from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
import os

from lib import selectProcess
from authenticate import isAllowed

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def respond():
    ACCOUNT_SID = "ACe892e28b309a94844845c5f621ca451a"
    AUTH_TOKEN = "99426e30a3c5c2e25d5ba56f9087b7c3"
    OUR_NUMBER = "+18442306122"


    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    userMessage = request.values.get( 'Body', None )
    userPhoneNumber = request.values.get( 'From', None)
    print(userPhoneNumber)

    resp = twilio.twiml.Response()

    if(isAllowed(userPhoneNumber)):
        ## Send raw user input for parsing and api use
        response = selectProcess( userMessage )
        resp.message(response)
    else:
        response = "Welcome to SMS, the premier web-surfing text message service!\n To gain access to our many features including Wikipedia lookup, Yelp, and Google Maps directions, please call 1-844-230-6122 to subscribe"
        resp.message(response)

    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
