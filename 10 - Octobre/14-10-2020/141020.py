# Non
def non(x):
    return 1-x

# Et
def et(x, y):
    return x*y

# Ou
def ou(x, y):
    return x+y-x*y

# Ou exclusif
def xou(x, y):
    return (x-y)**2

# On vérifie que xou(x,y) est égal à et(non(y),x) ou et(y, non(x))
def test_xou_et(x,y): # Renvoie True à chaque fois
    if (xou(x,y)==et(non(y),x)) or (xou(x,y)==et(y,non(x))):
        return True
    else:
        return False

# Non Et
def net(x,y):
    return non(x*y)

# Non Ou
def nou(x, y):
    return non(x+y-x*y)
