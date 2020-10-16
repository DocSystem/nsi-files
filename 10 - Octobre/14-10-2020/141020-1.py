# Fonctions
def non(x):
    return 1-x
def et(x, y):
    return x*y
def ou(x, y):
    return x+y-x*y
def oux(x, y):
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
#ex1()

# Exercice 2
def ex2():
    x=1
    y=1
    if (et(x,y)==non(ou(non(x), non(y)))):
        print("ET(x,y) = NON(NON(x) OU NON (y))")
    else:
        print("ET(x,y) != NON(NON(x) OU NON (y))")
#ex2()

# Exercice 3.1
def sheffer(x, y):
    return non(et(x,y))
# Exercice 3.2
def ex3_2():
    x=1
    if (non(x)==sheffer(x,x)):
        print("NON(x) = S(x, x)")
    else:
        print("NON(x) != S(x, x)")
#ex3_2()

# Exercice 4.1
def mux(x, y, z):
    return ou(et(x, y), et(non(x), z))

# Exercice 5.1
def ex5():
    x=1
    y=1
    z=1
    if (mux(x, y, z) == ou(et(non(x), y), et(x,z))):
        print("mux(x, y, z) = NON(x).y + x.z")
    else:
        print("mux(x, y, z) != NON(x).y + x.z")

# Exercice 6.1
def ex6():
    x=1
    y=1
    if (oux(x, y) == mux(y, oux(x, 0), oux(x, 1))):
        return True
    else:
        return False
