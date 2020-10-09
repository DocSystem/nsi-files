def somme(tuple):
    num = 0
    for i in tuple:
        num+=i
    print(num)
# somme([1, 2, 3])

def ex2():
    dictio = [
        {
            "name": "Tamim",
            "age": "666"
        },
        {
            "name": "Antoine",
            "age": "15"
        }
    ]
    for user in dictio:
        print(user["name"] + " a " + user["age"] + " ans")
# ex2()

def dict_vers_liste():
    dictio = [
        {
            "name": "Tamim",
            "age": "666"
        },
        {
            "name": "Antoine",
            "age": "15"
        }
    ]
    ls = []
    for user in dictio:
        ls.append((user["name"], user["age"]))
    print(ls)
# dict_vers_liste()

def liste_vers_dict():
    list = [("Tamim", "666"), ("Antoine", "15")]
    dictio = []
    for user in list:
        dictio.append({"name": user[0], "age": user[1]})
    print(dictio)

# liste_vers_dict()

def compter_mots(string):
    wordnum = {}
    for wordlist in string.split():
        wordnum[wordlist] = 0
        for word in string.split():
            if word==wordlist:
                wordnum[wordlist]+=1
    for word in wordnum:
        print(word + " : " + str(wordnum[word]))
# compter_mots("Salut moi moi c'est Mickey")

def compter_mots_par_antoine_lol(string):
    print(len(string.split()))
# compter_mots_par_antoine_lol("Salut moi c'est Mickey LOL")

def cesar(string):
    charlist = list(string.upper())
    newcharlist = []
    for c in charlist.upper():
        if ord(c) + 2>90:
            newcharlist.append(chr(ord(c) + 2 - 26))
        else:
            newcharlist.append(chr(ord(c) + 2))
    print("".join(newcharlist))
# cesar("QYJSR")

def vigenere(string, key):
    charlist = list(string.upper())
    keylist = []
    for c in key.upper():
        keylist.append(ord(c) - 65)
    newcharlist = []
    for c in range(len(charlist)):
        if ord(charlist[c]) + keylist[c%len(keylist)] > 90:
            newcharlist.append(chr(ord(charlist[c]) + keylist[c%len(keylist)] - 26))
        else:
            newcharlist.append(chr(ord(charlist[c]) + keylist[c%len(keylist)]))
    print("".join(newcharlist))
# vigenere("QYJSR", "CBCCC")

def decoder(string, key):
    charlist = list(string.upper())
    keylist = []
    for c in key.upper():
        keylist.append(ord(c) - 65)
    newcharlist = []
    for c in range(len(charlist)):
        if ord(charlist[c]) + keylist[c%len(keylist)] < 65:
            newcharlist.append(chr(ord(charlist[c]) - keylist[c%len(keylist)] + 26))
        else:
            newcharlist.append(chr(ord(charlist[c]) - keylist[c%len(keylist)]))
    print("".join(newcharlist))
decoder("SZLUT", "CBCCC")
