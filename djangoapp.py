from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
 
app = Flask(__name__)

def send_message();
    client.messages.create(
        to=userNumber,
        from_=OUR_NUMBER,
        body=response,
        media_url=media_response,
    )


#from Twilio acct
ACCOUNT_SID = "ACe892e28b309a94844845c5f621ca451a"
AUTH_TOKEN = "[99426e30a3c5c2e25d5ba56f9087b7c3]"
OUR_NUMBER = "+18442306122"

#needs to be a string
userNumber= request.values.get( 'From', None )

@app.route("/", methods=['GET', 'POST'])

client = TwilioRestClient( ACCOUNT_SID, AUTH_TOKEN )

while true:
    clientMessages = client.messages.list( to=OUR_NUMBER )
    for m in clientMessages:
        if m.status == "receiving":
            #do the things
            userNumber=m.From
            response= m.status
            send_message()
        if m.status == "undelivered" or m.status == "failed":
            #TBD

response = "4321"
media_response = ""

send_message()

if __name__ == "__main__":
    port = int( os.environ.get( "PORT",5000 ) )           
    app.run(host="0.0.0.0", port=port)
