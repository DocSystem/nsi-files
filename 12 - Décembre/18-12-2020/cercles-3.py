from tkinter import *
from math import *
import random
import time

Nombre_Cases=10
DIM_CASE=40   # dimensions du carre representant une case du plateau
app = Tk()
app.geometry("900x900")
can = Canvas(app, width = Nombre_Cases*DIM_CASE, height = Nombre_Cases*DIM_CASE, background = 'white')
can1=Canvas(app,bg="light gray",width = Nombre_Cases*DIM_CASE, height = Nombre_Cases*DIM_CASE)
can.pack()
can1.pack()

Plateau=[[0,"white"] for i in range(Nombre_Cases**2)]

Plateau[0]=[1, 'red']
Plateau[10]=[1, 'red']
Plateau[21]=[1,'yellow']
Plateau[15]=[1,'yellow']
Plateau[31]=[1,'yellow']
Plateau[35]=[1,'yellow']

##la fonction voisinsBis donne pour chaque case du plateau la
##liste de ses voisins

def deplacer(I):

    for J in range(Nombre_Cases**2):
        if Plateau[J][0]==1:
            dessiner_cercle(J,Plateau[J][1])
    if I>5:

        for J in range(Nombre_Cases**2):
            if Plateau[J][1]=='yellow':
                Plateau[J][0]==0
                dessiner_rectangle(J,'white')
                dessiner_cercle_2(J,Plateau[J][1])
    #if J%2==0:
#    dessiner_cercle(15,'red')
#    # elif J%2==1:
#    if J >5:
#       dessiner_cercle_2(15,'yellow')

## La fonction  dessiner_cercle dessine un cercle à l'intérieur
## d'une case

def dessiner_cercle(J,couleur):
# On récupère les "coordonnées" (en fait le numero de ligne et le numero de colonne)  de la case numéro J
    a= ( (J % Nombre_Cases) ,(J // Nombre_Cases))
    # x et y sont les coordonnées du coin supérieur gauche de la case
    x,y = a[0],a[1]
    can.create_oval(x*DIM_CASE, y*DIM_CASE, (x+1)*DIM_CASE,(y+1)*DIM_CASE, fill=couleur)

def dessiner_cercle_2(J,couleur):
# On récupère les "coordonnées" (en fait le numero de ligne et le numero de colonne)  de la case numéro J
    a=((J%Nombre_Cases),(J // Nombre_Cases))
    # x et y sont les coordonnées du coin supérieur gauche de la case
    x,y = a[0],a[1]
    can1.create_oval(x*DIM_CASE, y*DIM_CASE, (x+1)*DIM_CASE,(y+1)*DIM_CASE, fill=couleur)

def dessiner_rectangle(J,couleur):
# On récupère les "coordonnées" (en fait le numero de ligne et le numero de colonne)  de la case numéro J
    a= ( (J %Nombre_Cases) ,(J //Nombre_Cases))
    # x et y sont les coordonnées du coin supérieur gauche de la case
    x,y = a[0],a[1]
    can.create_rectangle(x*DIM_CASE, y*DIM_CASE,(x+1)*DIM_CASE,(y+1)*DIM_CASE, fill=couleur)

def Tracer_plateau():
    t=DIM_CASE
    can.delete(ALL)
    can1.delete(ALL)
#     Création de l'espace occupé par le futur plateau
    for i in range (Nombre_Cases) :
#         On créé les lignes
        can.create_line(0, i*t, Nombre_Cases*t, i*t)
#         On créé les colonnes
        can.create_line(i*t, 0, i*t, Nombre_Cases*t)
    for i in range (Nombre_Cases) :
#         On créé les lignes
        can1.create_line(0, i*t, Nombre_Cases*t, i*t)
#         On créé les colonnes
        can1.create_line(i*t, 0, i*t, Nombre_Cases*t)

    can.create_rectangle(1,1,Nombre_Cases*t,Nombre_Cases*t)  #un

    can.place(x=0,y=0)
    can1.place(x=500,y=0)

    deplacer(I)

I=0

def tourner():
    global I
    I=I+1

    #time.sleep(2)
    Tracer_plateau()
    app.after(200, tourner)

##Le programme principal.

tourner()

app.mainloop()
