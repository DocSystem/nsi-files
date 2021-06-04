def puissance_rapide(a, n):
    p=1
    b=a
    m=n
    while m>0:
        if m%2==1:
            p*=b
    b=b**2
    m=m**2
    return p

print(puissance_rapide(2, 3))
