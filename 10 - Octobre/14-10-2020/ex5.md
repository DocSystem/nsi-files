# Exercice 5

*Pour la fonction* ``mux(x,y,z)``*, voir [exercice 4](ex4.md)*

## Exercice 5.1

La fonction ``mux(x,y,z)`` renvoie la fonction suivante : ``ou(et(non(x), z), et(x, y))``,

Ce qui équivaut à x̅.z + x.y

## Exercice 5.2

```py
if (mux(x, y, z) == ou(et(non(x), z), et(x,y))):
  print("mux(x, y, z) = x̅.z + x.y")
else:
  print("mux(x, y, z) != x̅.z + x.y")
```
