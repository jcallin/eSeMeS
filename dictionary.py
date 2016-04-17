from PyDictionary import PyDictionary

def dictionary(command):
    dictionary = PyDictionary()
    words = command.split()

    choice = words[0]
    word = str(words[-1])

    print(choice)
    print(word)
    try:
        if choice == "define":
            definition = str(dictionary.meaning(word))
            return(definition)
        elif choice == "synonyms":
            synonyms = dictionary.synonym(word, "html5lib")
            result = ', '.join(synonyms)
            print(result)
            return result
        elif choice == "antonyms":
            antonyms = dictionary.antonym(word, "html5lib")
            result = ', '.join(antonyms)
            print(result)
            return result
        else:
            return "Please retry your question"
    except TypeError:
        return ("Your word had no " + choice)
