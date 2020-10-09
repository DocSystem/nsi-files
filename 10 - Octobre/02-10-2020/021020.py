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
    can.create_text(x*scale+0.5*scale,y*scale+0.5*scale,text=text,font="Arial14")
def tableau_aleatoire():
    L_nombres=list(range(100))
    D_nombres={}
    for x in range(10):
        for y in range(10):
            i = randint(0, len(L_nombres)-1)
            n = L_nombres[i]
            del L_nombres[i]
            D_nombres[(x,y)]=n
    return D_nombres

def carre_magique():
    L_nombres=list(range(Nombre_de_cases**2))
    D_nombres={}
    D_nombres[(2,0)]=1
    return D_nombres

def grille():
    initialisation()
    #tbl = tableau_aleatoire()
    tbl = carre_magique()
    for i in tbl:
        mettre_texte(i[0],i[1],tbl[i])
    can.pack()
    fen.mainloop()
grille()
