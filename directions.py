sourceKeyword = " from "
destinationKeyword = " to "
destinationSeperator = "with"
googleMapsApiKey = 'AIzaSyAPBGZ_K6NGbWnCup_lLO8Tk1fR1m_M2SU'

def getURL(source, destination, mode):
    url = 'https://maps.googleapis.com/maps/api/directions/json?origin='
    url += source
    url += "&destination="
    url += destination
    url += "&mode="
    url += mode
    url += "&key="
    url += "AIzaSyAPBGZ_K6NGbWnCup_lLO8Tk1fR1m_M2SU"
    return (url)

def getDirections(source, destination, mode):
    print( "test1" )
    url = getURL(source, destination, mode)
    print( "test2" )
    r = requests.get(url)   
    print( "test3" )
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
    return (out)


def directions(command):
    commandParts = command.split(destinationSeperator)
    mainCommand = commandParts[0]
    mode = mainCommand.split(sourceKeyword)[0].strip()
    if (mode == "walk" or mode == "walking"): mode = "walking"
    elif(mode == "bike" or mode == "bicycling"): mode = "bicycling"
    elif(mode == "bus" or mode == "train" or mode == "buses" or mode =="trains" or mode == "transit"): mode = "transit"
    else: mode = "driving"

    source = mainCommand.split(sourceKeyword)[1].split(destinationKeyword)[0].strip()
    destination = mainCommand.split(destinationKeyword)[1].strip()
    print( source )
    print( destination )
    print( mode )
    return(getDirections(source, destination, mode))

