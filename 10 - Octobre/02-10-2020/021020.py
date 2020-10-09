import tkinter as tk
from random import *
Nombre_de_cases=5
Hauteur=300
Largeur=300
scale=Hauteur/Nombre_de_cases
def initialisation():
    global fen,can,entree
    fen=tk.Tk()
    can=tk.Canvas(fen,bg="light gray", height=Hauteur,width=Largeur)
    quadrillage()
def quadrillage():
    L=Hauteur/scale+1
    l=Largeur/scale+1
    for i in range(0,int(l+1)):
        can.create_line(0,scale*i,scale*(L-1),scale*i,fill="black")
    for j in range(0,int(L)):
        can.create_line(scale*j,0,scale*j,scale*l,fill="black")
def noircir(x,y):
    can.create_rectangle(x*scale,y*scale,x*scale+scale,y*scale+scale,fill="violet")
def effacer(x,y):
    can.create_rectangle(x*scale,y*scale,x*scale+scale,y*scale+scale,fill="light gray")
def mettre_texte(x,y,text):
    can.create_text(x*scale+0.5*scale,y*scale+0.5*scale,text=text,font="Arial14") # Sert à mettre du texte (argument text) dans une case choisie (arguments x et y)
def tableau_aleatoire():
    L_nombres=list(range(100)) # On crée une liste avec les nombres de 0 à 99
    D_nombres={} # On crée un dictionnaire pour sauvegarder les cases
    for x in range(10): # On itère 10 fois pour 10 positions x différentes
        for y in range(10): # On itère 10 fois pour 10 positions y différentes
            i = randint(0, len(L_nombres)-1) # On prend un emplacement au hasard dans la liste des nombres
            n = L_nombres[i] # On sauvegarde le nombre à l'emplacement choisi dans la variable n
            del L_nombres[i] # On supprime le nombre à l'emplacement choisi de la liste des nombres afin qu'il ne soit pas re-choisi plus tard
            D_nombres[(x,y)]=n # On sauvegarde le nombre et son emplacement dans le dictionnaire des cases
    return D_nombres # On renvoit le dictionnaire des cases

def carre_magique():
    L_nombres=list(range(Nombre_de_cases**2))
    D_nombres={}
    D_nombres[(2,0)]=1
    return D_nombres

def grille():
    initialisation()
    tbl = tableau_aleatoire() # On sauvegarde le dictionnaire renvoyé par la fonction pour créer un tableau aleatoire dans une variable
    #tbl = carre_magique()
    for i in tbl: # On itère chaque élément du dictionnaire (qui correspond à chaque case)
        mettre_texte(i[0],i[1],tbl[i]) # On mets le texte de l'élément actuel dans la case aux coordonnées correspondantes
    can.pack()
    fen.mainloop()
grille()
