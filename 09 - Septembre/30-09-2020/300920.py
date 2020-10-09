# Exercice 1

def A_calcul(u=0):
    i=0
    while u<20:
        i+=1
        u=2*u+1
    return i

#print(A_calcul(1))

"""
Questions
1. La fonction prend un argument optionnel
2. Elle retourne 31
3. Elle retourne 31 aussi
4. 4 multiplications
"""

# Exercice 2

def imp_calcul(n):
    L=[]
    i=0
    while i<n/4:
        L.append(4*i)
        i+=1
    return L

#print(imp_calcul(13))

"""
Questions
1. [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
"""

# Exercice 3

def ex_3():
    Dates_Naiss = {
        "Tim": "12/10/2017",
        "Tom": "5/1/2016",
        "Ello": "6/2/2016",
        "Ella": "30/3/2017"
    }
    for student in Dates_Naiss:
        #print(Dates_Naiss[student].split("/")[1])
        print(student + " : " + Dates_Naiss[student])

#ex_3()

# Exercice 4

def successeur(n):
    return n+1

#print(successeur(2))

def addition(p, q):
    for i in range(q):
        p=successeur(p)
    return p

#print(addition(2, 7))

def multiplication(p, q):
    x=0
    for i in range(p):
        for n in range(q):
            p=successeur(p)
    return p

#print(multiplication(1,6))

def factorielle(n):
    if n>0:
        x=1
        for i in range(n):
            x*=i+1
        return x
    else:
        return "Un truc chelou"
print(factorielle(-5))
