# Exercice 6

On ouvre le fichier :

```py
import csv

db = []

with open("libri.csv", newline="") as dbfile:
    dbreader = csv.DictReader(dbfile, delimiter=";")
    for row in dbreader:
        db.append(dict(row))
```

Ensuite on affiche les romans de Victor Hugo :

```py
titres = []
for entry in db:
    if (entry["genre"] == "roman") and (entry["auteur"] == "Hugo Victor"):
        titres.append(entry)
print(titres)
```
