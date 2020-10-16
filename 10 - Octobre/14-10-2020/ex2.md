# Exercice 2

* En code :

```py
x=1
y=1
if (et(x,y)==non(ou(non(x), non(y)))):
  print("ET(x,y) = NON(NON(x) OU NON (y))")
else:
  print("ET(x,y) != NON(NON(x) OU NON (y))")
```

* Le tableau :

| x | y | NON(x) | NON(y) | NON(x) OU NON(y) | Sortie |
|---|---|--------|--------|------------------|--------|
| 0 | 0 |   1    |   1    |         1        |   0    |
| 0 | 1 |   1    |   0    |         1        |   0    |
| 1 | 0 |   0    |   1    |         1        |   0    |
| 1 | 1 |   0    |   0    |         0        |   1    |
