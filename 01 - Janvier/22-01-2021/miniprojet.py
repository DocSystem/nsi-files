"""
Owners:
- Antoine Souben-Fink
- Victor Dubost
"""

def miniprojet():
    # Affichage du menu
    print("\033[36m========== Répertoire ==========\033[39m")
    print("\033[32m0\033[39m - \033[31mQuitter\033[39m")
    print("\033[32m1\033[39m - \033[32mAjouter une entrée\033[39m")
    print("\033[32m2\033[39m - \033[33mRechercher par nom\033[39m")
    print("\033[32m3\033[39m - \033[33mRechercher par age\033[39m")
    print("\033[36m================================\033[39m")
    # Choix de l'utilisateur
    userchoice = input()
    if (userchoice == "1"):
        miniprojet_add()
        miniprojet()
    elif (userchoice == "2"):
        miniprojet_search()
        miniprojet()
    elif (userchoice == "3"):
        miniprojet_byage()
        miniprojet()
    elif (userchoice != "0"):
        miniprojet()

# Récupérer le répertoire sous forme de liste de dictionnaires
def miniprojet_getrepertoire():
    f = open("repertoire.txt", "r")
    repertoire = []
    for l in f:
        l=l.strip("\n")
        infoarr = l.split(":")
        repertoire.append({"nom": infoarr[0], "numero": infoarr[1], "adresse": infoarr[2], "age": int(infoarr[3])})
    return repertoire

# Ajouter un contact au répertoire
def miniprojet_add():
    f = open("repertoire.txt", "a") # Ouvrir le fichier
    nom = input("\033[32mNom (0 pour retourner au menu)\033[39m : ")
    if (nom != "0"): # Si on rentre zéro la fonction s'arrête et on revient au menu
        num = input("\033[32mNuméro de téléphone\033[39m : ")
        adresse = input("\033[32mAdresse\033[39m : ")
        age = input("\033[32mAge\033[39m : ")
        f.write(nom + ":" + num + ":" + adresse + ":" + age + "\n") # On écrit dans le fichier du répertoire
        miniprojet_add() # On relance la fonction jusqu'a ce que l'utilisateur l'arrête en écrivant 0

# Recherche par nom dans le répertoire
def miniprojet_search():
    repertoire = miniprojet_getrepertoire() # On récupère le répertoire
    nom = input("\033[32mEntrez un nom à rechercher\033[39m : ")
    search_ok = False
    for contact in repertoire:
        if (contact["nom"] == nom): # Si le contact correspond au nom entré on affiche ses infos
            search_ok = True
            print(" ")
            print("\033[36m" + contact["nom"] + "\033[39m :")
            print("\033[32mNuméro\033[39m : " + contact["numero"])
            print("\033[32mAdresse\033[39m : " + contact["adresse"])
            print("\033[32mAge\033[39m : " + contact["age"])
            print(" ")
    if (search_ok != True):
        print("\033[31mInconnu\033[39m") # Si aucun contact ne correspond on affiche "Inconnu"
        print(" ")

def miniprojet_byage():
    repertoire = miniprojet_getrepertoire() # On récupère le répertoire
    print(" ")
    print("Recherche par age :")
    agemin = int(input("Age minimum : "))
    agemax = int(input("Age maximum : "))
    print(" ")
    print("Contacts ayant entre " + str(agemin) + " et " + str(agemax) + " ans :")
    for contact in repertoire:
        if ((contact["age"] >= agemin) and (contact["age"] <= agemax)):
            print(contact["nom"]) # Si le contact est contenu dans la tranche d'age rentrée on affiche son nom
    print(" ")

miniprojet() # On execute la fonction principale
