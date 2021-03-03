import pandas as pd

def menu():
    print("======================== MENU ========================")
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
    elif (r == "2"):
        noms_salaries_par_projet()
        menu()
    elif (r == "4"):
        noms_salaries_par_departement()
        menu()
    elif (r == "5"):
        salaries_par_ordre_ancienete()
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
    projetsdb = pd.read_csv("projets.csv", delimiter=";")
    cadresdb = pd.read_csv("cadres.csv", delimiter=";")
    noncadresdb = pd.read_csv("non_cadres.csv", delimiter=";")
    employesdb = pd.read_csv("employes.csv", delimiter=";")
    projets = {}
    for i in projetsdb.id:
        nom_projet = projetsdb[projetsdb.id == i].nom_projet.unique()[0]
        projets[nom_projet] = []
        cadres_projet = []
        for p in cadresdb.id_cadre:
            cadre = cadresdb[cadresdb.id_cadre == p]
            employe = employesdb[employesdb.id == p]
            nom = employe.nom.unique()[0] + " " + employe.prenom.unique()[0]
            liste_projets = cadre.liste_projets.unique()[0].split(",")
            for j in liste_projets:
                if (int(i) == int(j)):
                    projets[nom_projet].append(nom)
        for p in noncadresdb.id_noncadre:
            noncadre = noncadresdb[noncadresdb.id_noncadre == p]
            employe = employesdb[employesdb.id == p]
            nom = employe.nom.unique()[0] + " " + employe.prenom.unique()[0]
            liste_projets = noncadre.liste_projets.unique()[0].split(",")
            for j in liste_projets:
                if (int(i) == int(j)):
                    projets[nom_projet].append(nom)
    for proj in projets:
        print("Employés sur le projet " + proj + " :")
        for emp in projets[proj]:
            print("- " + emp)
        print(" ")


#def tri_par_moyens_humains():
    # Afficher les projets qui ont nécessité le plus de moyens humains

def noms_salaries_par_departement():
    employesdb = pd.read_csv("employes.csv", delimiter=";")
    print(" ")
    print("Nom des salariés par département :")
    print("1. Employes secteur informatique")
    print("2. Employes secteur mécanique")
    print("3. Employes secteur électronique")
    print("4. Employes secteur marketing")
    r = input("Que souhaitez vous faire : ")
    #if (r == "1"):

    #elif (r == "2"):

    #elif (r == "3"):

    #elif (r == "4"):


def salaries_par_ordre_ancienete():
    # Afficher les salariés par ordre d'ancienneté
    print(" ")
    print("Nom des salariés par ordre d'ancienneté :")
    employesdb = pd.read_csv("employes.csv", delimiter=";")
    anciens = employesdb.sort_values(by="date_embauche")
    print(anciens)

menu()
