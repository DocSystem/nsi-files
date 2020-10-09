def ex1(day,month,year):
    daybin=[]
    for i in bin(day).split('b')[1]:
        daybin.append(i)
    while len(daybin)<5:
        daybin.insert(0, '0')
    daybin="".join(daybin)
    monthbin=[]
    for i in bin(month).split('b')[1]:
        monthbin.append(i)
    while len(monthbin)<4:
        monthbin.insert(0, '0')
    monthbin="".join(monthbin)
    yearbin=[]
    for i in bin(year).split('b')[1]:
        yearbin.append(i)
    while len(yearbin)<11:
        yearbin.insert(0, '0')
    yearbin="".join(yearbin)
    finalbin=daybin+monthbin+yearbin
    print(finalbin)
#ex1(7,8,2005)

def ex2():
    a=54
    b=111
    a=bin(a).split("b")[1]
    b=bin(b).split("b")[1]
    print(a)
    print(b)
ex2()
