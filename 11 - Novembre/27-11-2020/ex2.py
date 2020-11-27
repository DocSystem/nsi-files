from random import randint

T = [
    [ 12, 11, 10 ],
    [ 3, 5, 48 ],
    [ 6, 14, 60 ],
    [ 4, 15, 16 ]
]

def plus_grand(tableau=[[]]):
    imax = tableau[0]
    for fi in tableau:
        for si in fi:
            if si>imax:
                imax=si
    return imax

#print(plus_grand(T))

def echange_premiere_derniere_ligne(tableau=[[]]):
    x = tableau[len(tableau)-1]
    tableau[len(tableau)-1] = tableau[0]
    tableau[0] = x
    return tableau

#print(echange_premiere_derniere_ligne(T))

def echange_deux_lignes(tableau=[[]], li1=1, li2=2):
    li1=li1-1
    li2=li2-1
    tmplist = tableau[li1]
    tableau[li1] = tableau[li2]
    tableau[li2] = tmplist
    return tableau

#print(echange_deux_lignes(T), 1, 2)

def echange_deux_colonnes(tableau=[[]], col1=1, col2=2):
    col1 = col1-1
    col2 = col2-1
    for row in tableau:
        tmpval = row[col1]
        row[col1] = row[col2]
        row[col2] = tmpval
    return tableau

#print(echange_deux_colonnes(T), 1, 2)
