import csv

pays = []

def readAsTable():
    with open("countries.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=";")
        for row in spamreader:
            pays.append(row)

def readAsDict():
    with open("countries.csv", newline="") as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=";")
        for row in spamreader:
            pays.append(dict(row))

def paysEnEuro():
    returnList = []
    for p in pays:
        if p["currency_code"] == "EUR":
            returnList.append(p["name"])
    return returnList

def paysEnDollars():
    returnList = []
    for p in pays:
        if p["currency_name"] == "Dollar":
            returnList.append(p["currency_code"])
    returnList = supprimerDoublons(returnList)
    return returnList

def supprimerDoublons(liste=[]):
    returnList = []
    for i in liste:
        if (i in returnList == False):
            returnList.append(i)
    return returnList

readAsDict()
