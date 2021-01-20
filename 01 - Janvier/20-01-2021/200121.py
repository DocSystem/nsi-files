def cours():
    f=open("unfichier.txt", "r")
    lecture=f.readlines()
    for ligne in lecture:
        print(ligne)
    f.close()

def ex1():
    n=[]
    f=open("notes.txt", "r")
    lecture=f.readlines()
    for i in lecture:
        n.append(float(i))
    return n

def ex2():
    n=ex1()
    f=open("notes2.txt", "w")
    for i in n:
        if i < 10:
            f.write(str(i) + " recalé\n")
        else:
            f.write(str(i) + " admis\n")
