from classe_celule_2 import Cellule

def nieme_element(n: int, lst: Cellule):
    """Renvoie le n-ieme element de la liste lst
    les elements sont numerotes a partir de 0"""
    if n <0 or lst is None:
        raise IndexError("Indice invalide")
    if n == 0:
        return lst.valeur
    else :
        return nieme_element(n - 1, lst.suivante)
     
# Tests
l2 = Cellule(3, Cellule(5, Cellule(1, None)))
assert nieme_element(0, l2) == 3