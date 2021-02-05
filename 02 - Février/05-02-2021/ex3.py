import pandas as pd
df1 = pd.read_csv("auteurs.csv", delimiter=";")
df2 = pd.read_csv("libri-bis.csv", delimiter=";")

# Question 1
resultat = pd.merge(left=df1, right=df2, left_on="auteur_id", right_on="auteur")

# Question 2
print("Noms et titres des auteurs")
print(resultat[["nom", "titre"]])

print(" ")

# Question 3 / 4
print("Noms des auteurs de nationalité française :")
print(resultat[resultat.nationalite == "français"].nom.unique())

print(" ")

# Question 5
print("Noms des écrivains ayant écrit des romans :")
print(resultat[resultat.genre == "roman"].nom.unique())

print(" ")

# Question 6
print("Noms des auteurs ayant écrit des livres après 1900 :")
print(resultat[resultat.date > 1900].nom.unique())

print(" ")

# Question 7
print("Noms des auteurs de nationalité française ayant écrit des romans :")
print(resultat[(resultat.nationalite == "français")&(resultat.genre == "roman")].nom.unique())
