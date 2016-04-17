from PyDictionary import PyDictionary

def dictionary(command):
    dictionary = PyDictionary()
    words = command.split()

    choice = words[0]
    word = words[1]

    if choice == "define":
        return dictionary.meaning(word)
    elif choice == "synonym":
        synonyms = dictionary.synonym(word)
        result = ','.join(synonyms)
        return result
    elif choice == "antonym":
        antonyms = dictionary.antonym(word)
        result = ','.join(antonyms)
        return result
    else:
        return "Please retry your question"
