"""
Exercice 1
"""

L = [17,12,15,21,6,8]

def indice_max(list=[]):
    imax = list[0]
    for i in list:
        if i>imax:
            imax=i
    return imax

#print(indice_max(L))

def indice_min(list=[]):
    imin = L[0]
    for i in list:
        if i<imin:
            imin=i
    return imin

#print(indice_min(L))

def sort_list(list=[]):
    for index in range(1,len(list)):
        value = list[index]
        i = index-1
        while i>=0:
            if value < list[i]:
                list[i+1] = list[i]
                list[i] = value
                i -= 1
            else:
                break
    return list

#print(sort_list(L))
