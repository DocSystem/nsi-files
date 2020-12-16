from tkinter import *
import tkinter.font
from random import randint
from copy import deepcopy
import time

Nombre_de_cases=10
Hauteur=400
Largeur=400
scale=Hauteur/Nombre_de_cases

L=Hauteur/scale+1
l=Largeur/scale+1

def tri_a_bulles(liste):
    L=liste.copy()
    n=len(L)
    for i in range(-1, n):
        for j in range(n-1,i+1,-1):
            if L[j]["len"] < L[j-1]["len"]:
                L.insert(j, L.pop(j-1))
    return L

def initialisation():
    global fen , can ,can1
    fen = Tk()
    fen.title("algorithmes de tris")
    fen.geometry("900x900")
    #fen=tk.Tk()
    can=Canvas(fen,bg="light gray",height=Hauteur,width=Largeur)
    can1=Canvas(fen,bg="light gray",height=Hauteur,width=Largeur)
    quadrillage()

def quadrillage():
    for i in range(0 , int(l+1)):
        can.create_line(0,scale*i,scale*(L-1),scale*i,fill="black")
    for j in range(0 , int(L)):
        can.create_line(scale*j,0,scale*j,scale*l,fill="black")
    for i in range(0 , int(l+1)):
        can1.create_line(0,scale*i,scale*(L-1),scale*i,fill="black")
    for j in range(0 , int(L)):
        can1.create_line(scale*j,0,scale*j,scale*l,fill="black")

def remplir(x,y,coul,cadre):
    cadre.create_rectangle(x*scale,y*scale,(x+1)*scale,(y+1)*scale,fill=coul)

def effacer(x,y):
    can.create_rectangle(x*scale,y*scale,(x+1)*scale,(y+1)*scale, fill="light gray")

liste=[
    {
        "color": "light blue",
        "len": 5
    },
    {
        "color": "light green",
        "len": 8
    },
    {
        "color": "orange",
        "len": 2
    },
    {
        "color": "yellow",
        "len": 3
    },
    {
        "color": "aqua",
        "len": 7
    },
    {
        "color": "purple",
        "len": 4
    },
    {
        "color": "pink",
        "len": 6
    },
    {
        "color": "brown",
        "len": 10
    },
    {
        "color": "red",
        "len": 1
    },
    {
        "color": "white",
        "len": 9
    }
]

liste_triee=tri_a_bulles(liste)

def grille():
    initialisation()
    can.place(x=0,y=0)
    can1.place(x=500,y=0)
    for icolbar in range(len(liste)):
        colbar=liste[icolbar]
        for x in range(colbar["len"]):
            remplir(x,icolbar,colbar["color"],can)
    for icolbar in range(len(liste_triee)):
        colbar=liste_triee[icolbar]
        for x in range(colbar["len"]):
            remplir(x,icolbar,colbar["color"],can1)
    fen.mainloop()
grille()
