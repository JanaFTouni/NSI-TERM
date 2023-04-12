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
    for _ in range(n,0, -1):
        lst = Celulle(cpt, lst)
    return lst

def affiche_liste(lst : Cellule) -> None:
    if lst is None:
        print()
    else:
        print(lst.valeur, end = " ")
        affiche_liste(lst.suivante)
        
l1 = Cellule(5,Cellule(2, Cellule(7, Cellule(4, None))))


def affiche_liste(lst: Cellule) -> None:
    courant = lst
    while courant is not None:
        print(courant.valeur, end = " ")
        courant = courant.suivante
    print()
    

def nieme_element(n: int, lst: Cellule):
    """Renvoie le n-ieme element de la liste lst
    les elements sont numerotes a partir de 0"""
    if n <0 or lst is None:
        raise IndexError("Indice invalide")
    if n == 0:
        return lst.valeur
    else :
        return nieme_element(n - 1, lst.suivante)
    
def nieme_element(n: int, lst: Cellule) -> None:
    courant = lst
    a = 0
    if n < 0 :
        raise IndexError("Indice invalide")
    while a < n and courant is not None:
        a += 1
        courant = courant.suivante
    if courant is None :
        raise IndexError("Indice invalide")
    return courant.valeur
        
l2 = Cellule(3, Cellule(5, Cellule(1, None)))
assert nieme_element(0, l2) == 3
        