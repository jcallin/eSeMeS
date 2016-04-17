from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import re

def getYelp(command):

    lowerCom = command.lower()

    searchType = re.findall(r'yelp (.*?) in', lowerCom, re.DOTALL)
    searchKey=""
    for t in searchType:
        searchKey+=t
    searchType=searchKey	
    params = {
            'term' : searchType
            }

    keyword = 'in '
    before_key, keyword, after_key = lowerCom.partition(keyword)
    location = after_key

    auth = Oauth1Authenticator(
        consumer_key = "YOUR AUTH KEY",
        consumer_secret="YOUR AUTH KEY",
        token="YOUR TOKEN",
        token_secret="YOUR TOKEN SECRET",
    )

    client = Client(auth)

    response = client.search(location, **params)

    out =""
    for x in range(0,3):
        out += str(x+1) + ". " + str(response.businesses[x].name) + "\n Address: " + str(response.businesses[x].location.display_address).strip('[]').replace("'","").replace(",","") + "\n Ratings: " + str(response.businesses[x].rating) + " with " + str(response.businesses[x].review_count) + " Reviews \n Phone: " + str(response.businesses[x].display_phone) + "\n"
    return(out)
