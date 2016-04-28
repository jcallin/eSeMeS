import googlemaps
import json
import requests
import string
import re
import sys
import time

from datetime import datetime

sourceKeyword = " from "
destinationKeyword = " to "
destinationSeperator = "with"

def getURL(source, destination, mode, google_authkeys):
    url = 'https://maps.googleapis.com/maps/api/directions/json?origin='
    url += source
    url += "&destination="
    url += destination
    url += "&mode="
    url += mode
    url += "&key="
    url += google_authkeys["GOOGLE_API_KEY"]
    return (url)

def getDirections(source, destination, mode, google_authkeys):
    url = getURL(source, destination, mode, google_authkeys)
    r = requests.get(url)   
    obj = r.json()
    status = obj["status"]
    if status != "OK":
        return (1, "Error: bad status from Google Maps!")

    distance = obj["routes"][0]["legs"][0]["distance"]["text"]
    duration = obj["routes"][0]["legs"][0]["duration"]["text"]
    out = "directions~" + str(distance) + ": " + str(duration)
    steps = obj["routes"][0]["legs"][0]["steps"]
    i = 1
    for step in steps:
        dist = step["distance"]["text"]
        dur = step["duration"]["text"]
        directions = step["html_instructions"]
        directions = re.sub("<[^>]*>", '', directions)
        out += ("~" + "> " + str(dist) + "\n" + str(directions).strip("\n"))
        i = i + 1   
    return (out)


def Directions(command, google_authkeys):
    commandParts = command.split(destinationSeperator)
    mainCommand = commandParts[0]
    mode = mainCommand.split(sourceKeyword)[0].strip()
    if (mode == "walk" or mode == "walking"): mode = "walking"
    elif(mode == "bike" or mode == "bicycling"): mode = "bicycling"
    elif(mode == "bus" or mode == "train" or mode == "buses" or mode =="trains" or mode == "transit"): mode = "transit"
    else: mode = "driving"

    source = mainCommand.split(sourceKeyword)[1].split(destinationKeyword)[0].strip()
    destination = mainCommand.split(destinationKeyword)[1].strip()
    directions = getDirections(source, destination, mode, google_authkeys)
    return(directions)
