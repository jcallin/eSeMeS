import wikipedia
import string

def searchWiki( command ):
    keyword = command.split()[0]
    words = command.split(keyword)[1]

    page = wikipedia.page( words )
    content = page.summary
    content = filter(lambda x: x in string.printable, content )

    response=""
    for i in content:
        response += i
    print( response )
    return( response )
