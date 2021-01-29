# Exercice 5

On ouvre le fichier :

```py
import csv

db = []

with open("libri.csv", newline="") as dbfile:
    dbreader = csv.DictReader(dbfile, delimiter=";")
    for row in dbreader:
        db.append(dict(row))
```

Ensuite on affiche les oeuvres de Flaubert :

```py
titres = []
for entry in db:
    if (entry["auteur"] == "Flaubert Gustave"):
        titres.append(entry)
print(titres)
̀ ``
