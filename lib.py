import googlemaps
import json
import requests
import string
import re
import sys
import time

from datetime import datetime
from directions import directions
from dictionary import dictionary


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
    else: return False

def dictionaryCommand(command):
    if "define" in command: return True
    elif "synonyms" in command: return True
    else: return False

def browseCommand(command):
    if "http://" in command: return True
    elif "browse" in command: return True
    else: return False

def newsCommand(command):
    if "news" in command: return True
    elif "update" in command: return True
    else: return False

####Choose appropriate response based on command type####
def selectProcess(command):
    #commandList = re.sub("[^\w]", " ",  commandInput.lower()).split()
    if (directionCommand(command)):
        print("you have inputted a directions command")
        return(directions(command))
    elif(dictionaryCommand(command)):
        print("You have inputted a search command")
        return(dictionary(command))
    elif(browseCommand(command)):
        print("You have inputted a browse command")
        #getBrowseResults function
    elif (newsCommand(command)):
        print("You have inputted a news command")
        #getNewsResults Function
    else:
        return ("Invalid query")
        #return invalid querey message
