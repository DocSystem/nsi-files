def trouver_valeur(L=[], v=0):
    for i in L:
        if v==i:
            return True
    return False

liste=[1,2,3,4,5]
x=6

if trouver_valeur(liste, x):
    print("La liste contient " + str(x))
else:
    print("La liste ne contient pas " + str(x))
