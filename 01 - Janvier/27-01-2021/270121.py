import csv

pays = []

def readAsTable():
    with open("bornes-recharge-01.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=";")

readAsTable()
