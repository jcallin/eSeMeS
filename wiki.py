import wikipedia
import string

def SearchWiki( command ):
    keyword = command.split()[0]
    words = command.split(keyword)[1]

    page = wikipedia.page( words )
    content = page.summary
    returnText = content[0:400]
    content = filter(lambda x: x in string.printable, returnText)
    response=""
    for i in content:
        response += i
    response += "..." 

    return( response )
