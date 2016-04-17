sourceKeyword = " from "
destinationKeyword = " to "
destinationSeperator = "with"
googleMapsApiKey = 'AIzaSyAPBGZ_K6NGbWnCup_lLO8Tk1fR1m_M2SU'

def getURL(source, destination):
    url = 'https://maps.googleapis.com/maps/api/directions/json?origin='
    url += source
    url += "&destination="
    url += destination
    url += "&key="
    url += "AIzaSyAPBGZ_K6NGbWnCup_lLO8Tk1fR1m_M2SU"
    return (url)

def getDirections(source, destination):
    url = getURL(source, destination)
    r = requests.get(url)   
    obj = r.json()
    status = obj["status"]
    if status != "OK":
        return (1, "Error: bad status from Google Maps!")

    distance = obj["routes"][0]["legs"][0]["distance"]["text"]
    duration = obj["routes"][0]["legs"][0]["duration"]["text"]
    out = "directions~" + str(distance) + ";" + str(duration)
    steps = obj["routes"][0]["legs"][0]["steps"]
    i = 1
    for step in steps:
        dist = step["distance"]["text"]
        dur = step["duration"]["text"]
        directions = step["html_instructions"]
        directions = re.sub("<[^>]*>", '', directions)
        out += ("~" + str(dist) + "\n" + str(dur) + "--> " + str(directions))
        i = i + 1
    print(out)    
    return (out)

def directions(command):
    commandParts = command.split(destinationSeperator)
    mainCommand = commandParts[0]
    mode = mainCommand.split(sourceKeyword)[0].strip()
    source = mainCommand.split(sourceKeyword)[1].split(destinationKeyword)[0].strip()
    destination = mainCommand.split(destinationKeyword)[1].strip()
    print(source)
    print(destination)

    #if (commandParts[1]):
    #   options = commandParts[1]

    #if(options):
    #    if "alternatives" in options: alternatives = True
    #    else: alternaives = False

    #    if "less_walking" in options: routePreference = "less_walking"

    #    if "fewer_ransfers" in options: routePreference = "fewer_transfers"


    return(getDirections(source, destination))
        #def onDirectionsReturned(mssg):
        #mssgs = splitIntoMultipleMsgs(mssg)
        #sendResponse(mssg)
    
#steps = getDirections(mode, source, destination, alternatives, arrivalTime, departureTime, routePrefernce, googleMapsApiKey, onDirectionsReturned)

