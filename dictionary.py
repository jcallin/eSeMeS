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
            print("Returning your definition of " + word)
            definition = str(dictionary.getMeanings(word))
            print(definition)
            return(definition)
        elif choice == "synonyms":
            synonyms = dictionary.synonym(word)
            result = ', '.join(synonyms)
            return result
        elif choice == "antonyms":
            antonyms = dictionary.antonym(word)
            result = ', '.join(antonyms)
            return result
        else:
            return "Please retry your question"
    except TypeError:
        return ("Your word had no " + choice)
