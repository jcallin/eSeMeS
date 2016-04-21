from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
import os
import json

from lib import selectProcess
from authenticate import isAllowed

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def respond():

    # Replace  authkeys.json with your authkeys json file name
    # An example json file for storing authkeys is shown in the repository
    with open('authkeys.json') as authkeys_file:
        authkeys = json.load(authkeys_file)

    ACCOUNT_SID = authkeys["twilio"]["ACCOUNT_SID"]
    AUTH_TOKEN = authkeys["twilio"]["AUTH_TOKEN"]
    OUR_NUMBER = authkeys["twilio"]["OUR_NUMBER"]


    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    userMessage = request.values.get( 'Body', None )
    userPhoneNumber = str(request.values.get( 'From', None))

    resp = twilio.twiml.Response()

    ## Check if the user is subscribed
    if(isAllowed(userPhoneNumber)):
        response = selectProcess( userMessage )
        resp.message(response)
    else:
        response = "Welcome to SMS, the premier web-surfing text message service!\nTo gain access to our many features including Wikipedia lookup, Yelp, and Google Maps directions, please call 1-844-230-6122 and subscribe"
        resp.message(response)

    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
