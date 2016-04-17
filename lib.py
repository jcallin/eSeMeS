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
from placesNear import googlePlace


####Decide what kind of command has been inputted#####
def directionCommand(command):
    commands = ["walking", "walk", "directions", "bike", "biking", "drive", "driving", "car", "route", "bus", "transit", "train"]
    mode = command[0]
    if mode in commands:
        return True
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

def placesCommand(command):
    if command[0] == "look" and command[1] == "for":
        return True
    else:
        return False

def helpCommand(command):
    if command[0] == "?":
        return True
    else:
        return False

def printHelp():
    return ("Directions: '[mode] from [location] to [destination]'\nWikipedia: 'wiki [search term]'\nYelp lookup: 'yelp [service] in [location]'\nService lookup: 'find [service] near [zip]'\nRemember to use keywords!")

    

####Choose appropriate response based on command type####
def selectProcess(command):
    #commandList = re.sub("[^\w]", " ",  commandInput.lower()).split()
    commandList = command.lower().split()

    if (directionCommand(commandList)):
        print("you have input a directions command")
        return(directions(command))

    elif(dictionaryCommand(commandList)):
        print("You have input a dictionary command")
        return(dictionary(command))

    elif(yelpCommand(commandList)):
        print("You have input a yelp command")
        return(getYelp(command))

    elif (wikiCommand(commandList)):
        print("You have input a wiki command")
        return(searchWiki(command))
    elif(placesCommand(commandList)):
        print("You have input a places lookup command")
        return(googlePlace(command))
    elif(helpCommand(commandList)):
        print("You have input a help command")
        return(printHelp())

    else:
        return ("We didn't understand your search, see if this helps:\n" + printHelp())
