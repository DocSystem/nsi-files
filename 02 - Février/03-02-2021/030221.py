import pandas

pays = pandas.read_csv("countries.csv", delimiter=";", keep_default_na=False)

villes = pandas.read_csv("villes.csv", delimiter=";")
