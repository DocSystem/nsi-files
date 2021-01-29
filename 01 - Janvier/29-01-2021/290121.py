import csv

db = []

with open("libri.csv", newline="") as dbfile:
    dbreader = csv.DictReader(dbfile, delimiter=";")
    for row in dbreader:
        db.append(dict(row))

# Exercice 1
def cle_date(d):
    return d["date"]

def ex1():
    return sorted(db, key=cle_date)

# Exercice 2
def ex2():
    genres = []
    for entry in db:
        if (entry["genre"] not in genres):
            genres.append(entry["genre"])
    return genres

# Exercice 3
def ex3():
    titres = []
    for entry in db:
        if (int(entry["date"]) < 1820):
            titres.append(entry["titre"])
    return titres

# Exercice 4
def ex4():
    titres = []
    for entry in db:
        if (entry["genre"] == "roman") and (int(entry["date"]) > 1870):
            titres.append(entry)
    return titres

# Exercice 5
def ex5():
    titres = []
    for entry in db:
        if (entry["auteur"] == "Flaubert Gustave"):
            titres.append(entry)
    return titres

# Exercice 6
def ex6():
    titres = []
    for entry in db:
        if (entry["genre"] == "roman") and (entry["auteur"] == "Hugo Victor"):
            titres.append(entry)
    return titres

# Exercice 7
def ex7():
    sortdb = sorted(db, key=lambda entry: entry["date"])
    for entry in sortdb:
        if (entry["auteur"] == "Hugo Victor"):
            print(entry["titre"] + " : " + entry["date"])
