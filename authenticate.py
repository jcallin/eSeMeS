import string

def isAllowed(number):
    allowed=False
    with open("Numbers.txt") as f:
        content = f.readlines()
        for line in content:
            if number==line:
                allowed=True
    return( allowed )          
