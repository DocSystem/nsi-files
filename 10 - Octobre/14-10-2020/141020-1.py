# Fonctions
def non(x):
    return 1-x
def et(x, y):
    return x*y
def ou(x, y):
    return x+y-x*y
def xou(x, y):
    return (x-y)**2
def net(x,y):
    return non(x*y)
def nou(x, y):
    return non(x+y-x*y)

# Exercice 1
def ex1():
    x=1
    y=1
    if (ou(non(x),non(y))==non(et(x,y))):
        print("NON(x) OU NON(y) = NON(x ET y)")
    else:
        print("NON(x) OU NON(y) != NON(x ET y)")
        print("")
    if (et(non(x),non(y))==non(ou(x,y))):
        print("NON(x) ET NON(y) = NON(x OU y)")
    else:
        print("NON(x) ET NON(y) != NON(x OU y)")
ex1()
