import string

def isAllowed(number):
    allowed=False
    with open("Numbers.txt") as f:
        content = f.readlines()
        for line in content:
            if number == line.strip("\n"):
                allowed=True
                return(allowed)
    return( allowed )          
