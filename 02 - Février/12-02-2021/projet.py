import pandas as pd

def menu():
    print("=============== MENU ===============")
    print("1. Chiffre d'affaire par département")
    print("2. Noms des salariés par projet")
    print("3. Projets qui ont nécessité le plus de moyens humains")
    print("4. Nom des salariés qui travaillent dans un département")
    print("5. Salariés triés par ancienneté")
    print("6. Quitter")
    r = input("Que souhaitez vous faire : ")
    if (r == "1"):
        chiffre_affaires_par_departement()
        menu()
    elif (r != "6"):
        menu()

def chiffre_affaires_par_departement():
    print(" ")
    print("Chiffre d'affaires par département :")
    departementdb = pd.read_csv("departements.csv", delimiter=";")
    projetsdb = pd.read_csv("projets.csv", delimiter=";")
    chiffres_affaires = []
    for i in departementdb.id:
        departement = departementdb[departementdb.id == i]
        ca = 0
        liste_projets = departement.liste_projets.unique()[0].split(",")
        for projet in liste_projets:
            ca += projetsdb[projetsdb.id == int(projet)].chiffre_affaires.unique()[0]
        chiffres_affaires.append({"id": i, "ca": ca})
    for ca in chiffres_affaires:
        nom_dep = departementdb[departementdb.id == ca["id"]].nom_departement.unique()[0]
        chi_aff = ca["ca"]
        print(nom_dep + " : " + str(chi_aff) + "€")
    print(" ")

def noms_salaries_par_projet():
    print(" ")
    projet_nom = input("Nom du projet : ")
    print(" ")
    if (projet_nom != ""):
        

menu()
