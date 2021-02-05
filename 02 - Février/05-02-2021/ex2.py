import pandas as pd

# Question 1
df1 = pd.read_csv("auteurs.csv", delimiter=";")
df2 = pd.read_csv("libri-bis.csv", delimiter=";")

# Question 2
df2 = df2.sort_values(by="date")
df2 = df2.sort_values(by="ex")

# Question 3
print("Oeuvres publiées à partir de 1880 :")
print(df2[df2.date > 1880])

print(" ")

# Question 4
print("Oeuvres vendues à plus de 15 exemplaires")
print(df2[df2.ex > 15])

print(" ")

# Question 5
print("Nombre de romans : " + str(len(df2)))

print(" ")

# Question 6
nbr_ex = 0
for ex in df2.ex:
    nbr_ex += ex
print("Nombre total d'exemplaires : " + str(nbr_ex))
