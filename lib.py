import googlemaps
import json
import requests
import string
import re
import sys
import time
import wikipedia

from datetime import datetime
from directions import directions
from dictionary import dictionary
from wiki import searchWiki
from getYelp import getYelp


####Decide what kind of command has been inputted#####
def directionCommand(command):
    if "walking" in command: return True
    elif "walk" in command: return True
    elif "directions" in command: return True
    elif "bicycling" in command: return True
    elif "bike" in command: return True
    elif "drive" in command: return True
    elif "driving" in command: return True
    elif "car" in command: return True
    elif "train" in command: return True
    elif "bus" in command: return True
    elif "transit" in command: return True
    else: return False

def dictionaryCommand(command):
    if "define" in command: return True
    if "synonyms" in command: return True
    elif "antonyms" in command: return True
    else: return False

def yelpCommand(command):
    if command[0].lower() == "yelp":
        return True 
    else: return False

def wikiCommand(command):
    if command[0] == "wiki" or command[0] == "wikipedia":
        return True
    else: return False

####Choose appropriate response based on command type####
def selectProcess(command):
    #commandList = re.sub("[^\w]", " ",  commandInput.lower()).split()
    commandList = command.lower().split()

    if (directionCommand(commandList)):
        print("you have inputted a directions command")
        return(directions(command))

    elif(dictionaryCommand(commandList)):
        print("You have inputted a dictionary command")
        return(dictionary(command))

    elif(yelpCommand(commandList)):
        print("You have inputted a yelp command")
        return(getYelp(command))

    elif (wikiCommand(commandList)):
        print("You have inputted a wiki command")
        return(searchWiki(command))

    else:
        return ("Invalid query")
        #return invalid querey message
