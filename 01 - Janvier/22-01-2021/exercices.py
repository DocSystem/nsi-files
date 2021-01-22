def ex1():
    nom = input("Entrez un nom : ")
    f = open("fichier.txt", "a")
    f.write(nom)
    f.close()
    print("Fichier enregistré")

def ex2():
    f = open("fichier.txt", "r")
    contenu = f.read()
    f.close()
    print(contenu)

def ex3():
    f = open("fichier.txt", "a")
    for _ in range(5):
        nom = input("Entrez un nom : ")
        f.write(nom)
    f.close()
    print("Fichier enregistré")

def ex4():
    f = open("fichier.txt", "a")
    for _ in range(5):
        nom = input("Entrez un nom : ")
        f.write(nom + "\n")
    f.close()
    print("Fichier enregistré")

def ex5():
    f = open("fichier.txt", "r")
    noms = []
    for l in f:
        l=l.strip("\n")
        noms.append(l)
    print("Opération terminée")
    return noms
