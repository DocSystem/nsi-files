from tkinter import *
import tkinter.font
from random import randint
from copy import deepcopy
import time

Nombre_de_cases=10
Hauteur=400
Largeur=400
scale=Hauteur/Nombre_de_cases

Liste_mots=["chateau", "maison", "cabane", "mer", "montagne", "casino"]

L=Hauteur/scale+1
l=Largeur/scale+1

def tri_a_bulles(liste):
    L=liste.copy()
    n=len(L)
    for i in range(-1, n):
        for j in range(n-1,i+1,-1):
            if L[j] < L[j-1]:
                L.insert(j, L.pop(j-1))
    return L

Liste_triee=tri_a_bulles(Liste_mots)

print(Liste_mots)
print(Liste_triee)

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

def remplissage(A,y,t=1):
    for x in range(len(A)):
        if t==2:
            can1.create_text(x*scale+20,y*scale+20,text=str(A[x]), font="Arial 16")
        else:
            can.create_text(x*scale+20,y*scale+20,text=str(A[x]), font="Arial 16")

def remplir(x,y,coul,cadre):
    cadre.create_rectangle(x*scale,y*scale,(x+1)*scale,(y+1)*scale,fill=coul)

def effacer(x,y):
    can.create_rectangle(x*scale,y*scale,(x+1)*scale,(y+1)*scale, fill="light gray")

def grille():
    initialisation()
    can.place(x=0,y=0)
    can1.place(x=500,y=0)
    for imot in range(len(Liste_triee)):
        remplissage(Liste_triee[imot], imot)
    for imot in range(len(Liste_mots)):
        remplissage(Liste_mots[imot], imot, t=2)
    fen.mainloop()
grille()
