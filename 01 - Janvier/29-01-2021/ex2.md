# Exercice 2

On ouvre le fichier :

```py
import csv

db = []

with open("libri.csv", newline="") as dbfile:
    dbreader = csv.DictReader(dbfile, delimiter=";")
    for row in dbreader:
        db.append(dict(row))
```

Ensuite on trie par genre :

```py
genres = []
for entry in db:
    if (entry["genre"] not in genres):
        genres.append(entry["genre"])
print(genres)
```
