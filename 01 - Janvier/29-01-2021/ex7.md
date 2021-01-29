# Exercice 7

On ouvre le fichier :

```py
import csv

db = []

with open("libri.csv", newline="") as dbfile:
    dbreader = csv.DictReader(dbfile, delimiter=";")
    for row in dbreader:
        db.append(dict(row))
```

Ensuite on affiche les oeuvres de Victor Hugo triées par ordre chronologique :

```py
sortdb = sorted(db, key=lambda entry: entry["date"])
for entry in sortdb:
    if (entry["auteur"] == "Hugo Victor"):
        print(entry["titre"] + " : " + entry["date"])
```
