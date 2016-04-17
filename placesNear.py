from googleplaces import GooglePlaces, types, lang
import geocoder
import urllib
import json
import requests
import re

destinationSeperator="look for "
locationSeperator=" near "


apiKey="AIzaSyA43esVZvcufle30_kihWbBG1RfJ5M1P60"

def googlePlace(command):

    types = command.split(locationSeperator)[0].split(destinationSeperator)[1]
    zipCode = str(command.split(locationSeperator)[1])

    #making the url
    g = geocoder.google(zipCode)

    AUTH_KEY = "AIzaSyAPBGZ_K6NGbWnCup_lLO8Tk1fR1m_M2SU"
    LOCATION = str(g.latlng[0]) + "," + str(g.latlng[1])
    RADIUS = 1000
    TYPES = types
    url = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
           '?location=%s'
           '&radius=%s'
           '&types=%s'
           '&sensor=false&key=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY)
    #grabbing the JSON result
    response = requests.get(url)
    obj = response.json()
    results = obj["results"]

    def returnOpen(check):
        if(check==False):return "Currently closed"
        elif(check==True): return "Currently Open"
        elif(check is None): return "Hours Unknown"
        else:return

    out = "Nearby:\n"
    i = 1

    if(len(results) >=11):maxResults = 10
    else: maxResults=len(results)
    
    for i in range(0,maxResults):
        name = obj["results"][i]["name"]
        if('opening_hours' in obj["results"][i]):
            is_open = returnOpen(obj["results"][i]["opening_hours"]["open_now"])
        else: is_open = "Hours Unknown"
        address=  (obj["results"][i]["vicinity"])
        
        out +=("\n" + str(name) + "\n" + str(is_open) + "\n" + str(address) + "\n")
        i = i + 1
    
    print(out)
    return(out)
\

