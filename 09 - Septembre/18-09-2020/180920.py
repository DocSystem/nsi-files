from math import *

def ex1(ex):
    L1 = [i for i in range(4)]
    L2 = [i**2 for i in range(7) if (i**2)%3==1]
    if ex==1:
        L = L1+L2
        print(L)
    elif ex==2:
        L = []
        if len(L1)==len(L2):
            for i in range(len(L1)):
                n = L1[i] + L2[i]
                L.append(n)
        else:
            return None
        return L
