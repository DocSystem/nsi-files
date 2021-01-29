# Exercice 1

On ouvre le fichier :

```py
import csv

db = []

with open("libri.csv", newline="") as dbfile:
    dbreader = csv.DictReader(dbfile, delimiter=";")
    for row in dbreader:
        db.append(dict(row))
```

Ensuite on trie la liste :

```py
def cle_date(d):
    return d["date"]
sorted(db, key=cle_date)
```
