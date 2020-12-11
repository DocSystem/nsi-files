def tri_a_bulles(liste=[]):
    n=len(liste)
    for i in range(-1, n):
        for j in range(n-1,i+1,-1):
            if liste[j] < liste[j-1]:
                liste.insert(j, liste.pop(j-1))
    return liste

def tri_ordre_alphabetique(mot=""):
    lettreliste=[]
    motfinal=""
    for lettre in mot:
        lettreliste.append(ord(lettre))
    lettreliste=tri_a_bulles(lettreliste)
    for lettre in lettreliste:
        motfinal = motfinal + chr(lettre)
    print(motfinal)

tri_ordre_alphabetique("TIMEBIG")
