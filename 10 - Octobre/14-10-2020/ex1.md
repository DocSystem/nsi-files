# Exercice 1

* Pour NON(x) OU NON(y) = NON(x ET y) :

```py
if (ou(non(x),non(y))==non(et(x,y))):
  print("NON(x) OU NON(y) = NON(x ET y)")
else:
  print("NON(x) OU NON(y) != NON(x ET y)")
```

* Pour NON(x) ET NON(y) = NON(x OU y) :

```py
if (et(non(x),non(y))==non(ou(x,y))):
  print("NON(x) ET NON(y) = NON(x OU y)")
else:
  print("NON(x) ET NON(y) != NON(x OU y)")
```
