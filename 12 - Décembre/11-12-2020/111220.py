# Exercice 3 - Tri a bulles

def tri_a_bulles(L):
    L=liste
    n=len(L)
    for i in range(-1, n):
        for j in range(n-1,i+1,-1):
            if L[j] < L[j-1]:
                L.insert(j, L.pop(j-1))
    return L

# Exercice 5 - Tri des lettres d'un mot par ordre alphabétique

def tri_ordre_alphabetique(mot=""):
    lettreliste=[]
    motfinal=""
    for lettre in mot:
        lettreliste.append(ord(lettre))
    lettreliste=tri_a_bulles(lettreliste)
    for lettre in lettreliste:
        motfinal = motfinal + chr(lettre)
    return motfinal

#print(tri_ordre_alphabetique("ZYXWVUTSRQPONMLKJIHGFEDCBA"))

# Exercice 6 - Vérifier si un tableau est trié

def verifier_tableau_trie(L):
    n=len(L)
    for i in range(-1, n):
        for j in range(n-1,i+1,-1):
            if L[j] < L[j-1]:
                return False
    return True

#print(verifier_tableau_trie([2,1,3]))

# Exercice 7 - Insérer un élément dans une liste de façon à ce qu'elle soit triée

def insert_element_trie(cle=0, L=[]):
    n=len(L)
    for j in range(n-1,0,-1):
        if ((cle >= L[j-1]) and (cle <= L[j])):
            L.append(0)
            for item in range(n, j, -1):
                L[item]=L[item-1]
            L[j]=cle
            return L
        elif cle >= L[n-1]:
            L.append(cle)
            return L
        elif cle <= L[0]:
            L.append(0)
            for item in range(n, 0, -1):
                L[item]=L[item-1]
            L[0] = cle
            return L
    return L

print(insert_element_trie(4, [1,2,7,8]))
