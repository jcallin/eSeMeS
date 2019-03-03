# ESEMES ("ess-emm-ess")
## 1st place winner at Bronco Hack 2016 implementing basic information lookup through text message

### Set up a webserver to handle text messages with Twilio:
- Create a Twilio account and acquire a Twilio phone number to send text messages.
- Push our project to a webserver. Insert your API authkeys into authkeys.json for Yelp and Google, and Twilio.
- Add your phone number in a line at the top of Numbers.txt.
- Set up your Twilio phone number to forward all text messages it receives to your webserver's address. Run djangoapp.py on the webserver
- Send text messages to your Twilio number.

### Try it out:
Currently, we implement 4 query types: directions, wikipedia, yelp, and services (for stuff like hospitals, lawyers, etc)

Directions: `[Mode] from [location] to [destination]`
--Example "Driving from san jose to santa barbara"

Yelp: `Yelp [service] in [location]`
--Example "Yelp sushi in San Jose"

Services: `Find [service] near [zip code]`
--Example "Find hospital near 95050"
