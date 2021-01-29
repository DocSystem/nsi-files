import csv

pays = []

def readAsTable():
    with open("bornes-recharge-01.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=";")
        for row in range(len(spamreader)):
            pays.append(dict(spamreader[row]))
    return pays

print(readAsTable())
