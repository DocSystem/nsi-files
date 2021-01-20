def cours():
    f=open("unfichier.txt", "r")
    lecture=f.readlines()
    for ligne in lecture:
        print(ligne)
    f.close()

def ex1():
    n=[]
    m=0.0
    f=open("notes.txt", "r")
    lecture=f.readlines()
    for i in lecture:
        n.append(float(i))
        m+=float(i)
    m=m/len(n)
    return {"liste": n, "moyenne": m}

def ex2():
    n=ex1()["liste"]
    f=open("notes2.txt", "w")
    for i in n:
        if i < 10:
            f.write(str(i) + " recalé\n")
        else:
            f.write(str(i) + " admis\n")
