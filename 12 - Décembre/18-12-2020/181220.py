# =============== #
#     Imports     #
# =============== #

from tkinter import *
from math import *
import random
import time

# =============== #
#    Déf. vars    #
# =============== #

nombre_cases = 10 # Nombre de cases sur le plateau
taille_case = 40 # Taille d'une case
n = 0

# =============== #
#     Tableau     #
# =============== #

plateau = [[0,"white", 1] for _ in range(nombre_cases**2)] # Tableau
plateau[0] = [1, "red", 1]
plateau[12] = [1, "yellow", 0.5]
plateau[8] = [1, "yellow", 2]

# =============== #
#     Tkinter     #
# =============== #

app = Tk()
app.geometry("900x900")
can = Canvas(app, width=nombre_cases*taille_case, height=nombre_cases*taille_case, background='white')
can1 = Canvas(app, width=nombre_cases*taille_case, height=nombre_cases*taille_case)
can.pack()
can1.pack()

# =============== #
#    Fonctions    #
# =============== #

def tri_a_bulles(liste):
    L=liste.copy()
    n=len(L)
    for i in range(-1, n):
        for j in range(n-1,i+1,-1):
            if L[j]["len"] < L[j-1]["len"]:
                L.insert(j, L.pop(j-1))
    return L

def deplacer(n):
    for j in range(nombre_cases**2):
        if (plateau[j][0] == 1):
            dessiner_cercle(j, plateau[j][1], plateau[j][2])
    if n > 5:
        for j in range(nombre_cases**2):
            if plateau[j][1]=='yellow':
                plateau[j][0]==0
                if plateau[j][2] < 1:
                    dessiner_rectangle(j,'white', 1)
                else:
                    dessiner_rectangle(j,'white', plateau[j][2])
                dessiner_cercle_2(j,plateau[j][1], plateau[j][2])

def trier_par_taille(n):
    for j in range(nombre_cases**2):
        if (plateau[j][0] == 1):
            dessiner_cercle(j, plateau[j][1], plateau[j][2])
    if n > 5:
        for j in range(nombre_cases**2):
            if plateau[j][1]=='yellow':
                plateau[j][0]==0
                if plateau[j][2] < 1:
                    dessiner_rectangle(j,'white', 1)
                else:
                    dessiner_rectangle(j,'white', plateau[j][2])
                dessiner_cercle_2(j,plateau[j][1], plateau[j][2])

def dessiner_cercle(j, couleur, taille=1):
    a = ((j % nombre_cases), (j // nombre_cases)) # coordonnées (x, y) de la case
    x, y = a[0], a[1] # coordonnées haut gauche de la case
    can.create_oval(x*taille_case, y*taille_case, (x+taille)*taille_case, (y+taille)*taille_case, fill=couleur)

def dessiner_cercle_2(j, couleur, taille=1):
    a = ((j % nombre_cases), (j // nombre_cases)) # coordonnées (x, y) de la case
    x, y = a[0], a[1] # coordonnées haut gauche de la case
    can1.create_oval(x*taille_case, y*taille_case, (x+taille)*taille_case, (y+taille)*taille_case, fill=couleur)

def dessiner_rectangle(j, couleur, taille=1):
    a = ((j % nombre_cases), (j // nombre_cases)) # coordonnées (x, y) de la case
    x, y = a[0], a[1] # coordonnées haut gauche de la case
    can.create_rectangle(x*taille_case, y*taille_case, (x+taille)*taille_case, (y+taille)*taille_case, fill=couleur)

def tracer_plateau():
    t = taille_case
    can.delete(all)
    can1.delete(all)
    for i in range(nombre_cases):
        can.create_line(0, i*t, nombre_cases*t, i*t) # Lignes
        can.create_line(i*t, 0, i*t, nombre_cases*t) # Colonnes
    for i in range(nombre_cases):
        can1.create_line(0, i*t, nombre_cases*t, i*t) # Lignes
        can1.create_line(i*t, 0, i*t, nombre_cases*t) # Colonnes
    can.create_rectangle(1, 1, nombre_cases*t,nombre_cases*t)
    can.place(x=0, y=0)
    can1.place(x=500, y=0)
    deplacer(n)

def tourner():
    global n
    n+=1
    tracer_plateau()
    app.after(200, tourner)

tourner()
app.mainloop()
