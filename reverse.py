from classe_cellule import Cellule
from classe_cellule import longueur
from nieme_element  import nieme_element
from concat import concatenation

def renverser(lst: Celulle):
    """Renvoie un liste contenant les elements de lst dans l'ordre"""
    if lst is None:
        return None
    else:
        return concatenation(renverser(lst.suivante), Cellule(lst.valeur, None)) 


l1 = Cellule(1,Cellule(2, Cellule(3, None)))
l2 = renverser(l1)
assert l2.valeur == 3