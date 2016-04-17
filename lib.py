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
from wiki import searchWiki


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
    if "synonyms" in command: return True
    elif "antonyms" in command: return True
    else: return False

def browseCommand(command):
    if "http://" in command: return True
    elif "browse" in command: return True
    else: return False

def newsCommand(command):
    if "news" in command: return True
    elif "update" in command: return True
    else: return False

def wikiCommand(command):
    if "wiki" in command: return True
    elif "wikipedia" in command: return True
    else: return False

####Choose appropriate response based on command type####
def selectProcess(command):
    #commandList = re.sub("[^\w]", " ",  commandInput.lower()).split()
    commandList = command.split()

    if (directionCommand(commandList)):
        print("you have inputted a directions command")
        return(directions(command))

    elif(dictionaryCommand(commandList)):
        print("You have inputted a dictionary command")
        return(dictionary(command))

    elif(browseCommand(commandList)):
        print("You have inputted a browse command")

    elif (wikiCommand(commandList)):
        print("You have inputted a wiki command")
	return(searchWiki(command))

    else:
        return ("Invalid query")
        #return invalid querey message
