import tkinter as tk
Nombre_de_cases=3
Hauteur=150
Largeur=450
scale=Hauteur/Nombre_de_cases
def initialisation():
    global fen,can,entree
    fen=tk.Tk()
    can=tk.Canvas(fen,bg="light gray", height=Hauteur,width=Largeur)
    quadrillage()
    quadrillage2()
def quadrillage():
    L=Hauteur/scale+1
    l=Largeur/scale+1
    for i in range(0,int(l+1)):
        can.create_line(0,scale*i,scale*(L-1),scale*i,fill="black")
    for j in range(0,int(L)):
        can.create_line(scale*j,0,scale*j,scale*l,fill="black")
def quadrillage2():
    L=Hauteur/scale+1
    l=Largeur/(scale)+1
    for i in range(0,int(l+1)):
        can.create_line(300+i*scale,scale*(L-1),300+i*scale,0,fill="black")
    for j in range(0,int(L)):
        can.create_line(300, scale*j, 450, scale*j, fill="black")
def effacer(x,y):
    can.create_rectangle(x*scale,y*scale,x*scale+scale,y*scale+scale,fill="light gray")
def mettre_texte(x,y,text):
    can.create_text(x*scale+0.5*scale,y*scale+0.5*scale,text=text,font="Arial14") # Sert à mettre du texte (argument text) dans une case choisie (arguments x et y)

def echange_deux_colonnes(tableau=[[]]):
    col1 = 0
    col2 = len(tableau)-1
    for row in tableau:
        tmpval = row[col1]
        row[col1] = row[col2]
        row[col2] = tmpval
    return tableau

def grille():
    initialisation()
    tbl = [
        [ 12, 11, 10 ],
        [ 3, 5, 48 ],
        [ 6, 14, 60 ]
    ]
    for y in range(len(tbl)):
        for x in range(len(tbl[y])):
            mettre_texte(x,y,tbl[y][x])
    tbl = echange_deux_colonnes(tbl)
    for y in range(len(tbl)):
        for x in range(len(tbl[y])):
            mettre_texte(x+6,y,tbl[y][x])
    can.pack()
    fen.mainloop()
grille()
