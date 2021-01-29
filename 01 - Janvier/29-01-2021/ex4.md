# Exercice 4

On ouvre le fichier :

```py
import csv

db = []

with open("libri.csv", newline="") as dbfile:
    dbreader = csv.DictReader(dbfile, delimiter=";")
    for row in dbreader:
        db.append(dict(row))
```

Ensuite on affiche les romans publiés avant 1870 :

```py
titres = []
for entry in db:
    if (entry["genre"] == "roman") and (int(entry["date"]) > 1870):
        titres.append(entry)
print(titres)
```
