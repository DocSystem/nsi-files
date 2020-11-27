from tkinter import *
from random import randint
from copy import deepcopy
import time

Nombre_de_cases=10
Hauteur=400
Largeur=400
scale=Hauteur/Nombre_de_cases



L=[ [230,20,20],[220,40,20],[100,160,20],[100,200,20],[40,230,20],
[20,120,40],[20,150,40],[20,50,40],[20,20,230],[20,20,230]]


T=deepcopy(L)
L[0][0]=200
print(T[0][0])



def initialisation():
    global fen , can ,can1
    fen = Tk()

    fen.title("ESSAI AVEC CANVAS")

    fen.geometry("900x900")
    #fen=tk.Tk()
    can=Canvas(fen,bg="light gray",height=200,width=200)
    can1=Canvas(fen,bg="red",height=200,width=200)
    quadrillage()
#    for couple,valeur in tableau().items():
#            can.create_text(couple[0]*scale+35,couple[1]*scale+35,text=str(valeur),font="Arial14")

def quadrillage():
    L=Hauteur/scale+1
    l=Largeur/scale+1

    for i in range(0 , int(l+1)):
        can.create_line(0,scale*i,scale*(L-1),scale*i,fill="black")

    for j in range(0 , int(L)):
        can.create_line(scale*j,0,scale*j,scale*l,fill="black")

def remplir(x,y,coul,cadre):
    cadre.create_rectangle(x*scale,y*scale,(x+1)*scale,(y+1)*scale,fill=coul)

def effacer(x,y):
    can.create_rectangle(x*scale,y*scale,(x+1)*scale,(y+1)*scale,

                         fill="light gray")

def modifier(LC):
   D=deepcopy(LC)
   for x  in D:
       x[0]=250-x[0]
       x[1]=250-x[1]
       x[2]=250-x[2]
   return D


def colorier(LC,cadre):

     for x in range (Nombre_de_cases):
        #

        for y in range (Nombre_de_cases):
           #couleur="#{:x}{:x}{:x}".format(200,100,25)
           couleur="#{:x}{:x}{:x}".format(LC[x][0],LC[x][1],LC[x][2])
           remplir(x,y,couleur,cadre)


def grille():
    initialisation()
    colorier(L,can)
    can.place(x=0,y=0)

    LC=modifier(L)
    colorier(LC,can1)
    can1.place(x=600,y=0)

    fen.mainloop()

grille()
