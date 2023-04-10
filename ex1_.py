from classe_cellule import Cellule
from nieme_element  import nieme_element


# Écrire une fonction listeN(n) qui reçoit en argument un entier n,
# supposé positif ou nul, et renvoie la liste des entiers 1, 2, ... , n, dans cet ordre.
# Si n = 0, la liste renvoyée est vide.
# 
# Remarque : il faut utiliser l'implémentation d'une liste uniquement
# à partir de la classe Cellule. On ne pourra pas utiliser la classe Liste.

def listeN(n: int) -> Cellule:
    lst = None
    cpt = n
    for _ in tange(n,0, -1):
        lst = Celulle(cpt, lst)
    return lst
    