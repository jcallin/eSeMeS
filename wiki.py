import wikipedia
import string

def searchWiki( command ):
    words = command.split()
    word = words[1]

    page = wikipedia.page( word )
    content = page.summary
    content = filter(lambda x: x in string.printable, content )

    response=""
    for i in content:
        response += i
    return( response )
