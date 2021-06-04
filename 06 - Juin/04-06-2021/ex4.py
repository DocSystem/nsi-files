def euclide(a, b):
    x=a
    y=b
    while y!=0:
        temp=y
        y=x%y
        x=temp
    return x
