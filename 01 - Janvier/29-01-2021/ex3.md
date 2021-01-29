# Exercice 3

On ouvre le fichier :

```py
import csv

db = []

with open("libri.csv", newline="") as dbfile:
    dbreader = csv.DictReader(dbfile, delimiter=";")
    for row in dbreader:
        db.append(dict(row))
```

Ensuite on affiche les titres des oeuvres publiées avant 1820 :

```py
titres = []
for entry in db:
    if (int(entry["date"]) < 1820):
        titres.append(entry["titre"])
print(titres)
```
