import pandas as pd

# Exercice 1
def ex1():
    table_1 = pd.DataFrame({
        "id": ["1", "2", "3", "4"],
        "ecrivain": ["Hugo", "Boileau", "Rimbaud", "Voltaire"],
        "siècle": ["19", "17", "19", "18"]
    })

    table_2 = pd.DataFrame({
        "titre": ["les misérables", "candide", "illuminations", "rudiments", "Mme Bovary"],
        "genre": ["roman", "conte", "poème", "poème", "roman"],
        "id": ["1", "4", "3", "2", "6"]
    })
    resultat = pd.merge(left=table_1, right=table_2, on="id")
    return resultat

# 1ère question de l'exercice 1
def ex1q1():
    table_1 = pd.DataFrame({
        "id": ["1", "2", "3", "4"],
        "ecrivain": ["Hugo", "Boileau", "Rimbaud", "Voltaire"],
        "siècle": ["19", "17", "19", "18"]
    })

    table_2 = pd.DataFrame({
        "titre": ["les misérables", "candide", "illuminations", "rudiments", "Mme Bovary"],
        "genre": ["roman", "conte", "poème", "poème", "roman"],
        "auteur": ["1", "4", "3", "2", "6"]
    })
    resultat = pd.merge(left=table_1, right=table_2, left_on="id", right_on="auteur")
    return resultat

# 1ère partie de la 2e question de l'exercice 1 (avec how="left")
def ex1q2p1():
    table_1 = pd.DataFrame({
        "id": ["1", "2", "3", "4"],
        "ecrivain": ["Hugo", "Boileau", "Rimbaud", "Voltaire"],
        "siècle": ["19", "17", "19", "18"]
    })

    table_2 = pd.DataFrame({
        "titre": ["les misérables", "candide", "illuminations", "rudiments", "Mme Bovary"],
        "genre": ["roman", "conte", "poème", "poème", "roman"],
        "auteur": ["1", "4", "3", "2", "6"]
    })
    resultat = pd.merge(left=table_1, right=table_2, how="left", left_on="id", right_on="auteur")
    return resultat

# 2e partie de la 2e question de l'exercice 1 (avec how="right")
def ex1q2p2():
    table_1 = pd.DataFrame({
        "id": ["1", "2", "3", "4"],
        "ecrivain": ["Hugo", "Boileau", "Rimbaud", "Voltaire"],
        "siècle": ["19", "17", "19", "18"]
    })

    table_2 = pd.DataFrame({
        "titre": ["les misérables", "candide", "illuminations", "rudiments", "Mme Bovary"],
        "genre": ["roman", "conte", "poème", "poème", "roman"],
        "auteur": ["1", "4", "3", "2", "6"]
    })
    resultat = pd.merge(left=table_1, right=table_2, how="right", left_on="id", right_on="auteur")
    return resultat
