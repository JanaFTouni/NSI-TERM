from classe_celule_2 import Cellule
from classe_celule_2 import longueur
from nieme import nieme_element 


#recursivite

def concatenation(l1: Cellule, l2: Cellule) -> Cellule:
    """Concatene les listes l1 et l2,
    sous forme d'une nouvelle liste"""
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    else:
        return Cellule(l1.valeur, concatenation(l1.suivante, l2))
    
    
    
l1 = Cellule(1, Cellule(2, Cellule(3, None)))
l2 = Cellule(4, Cellule(5, None))
l3 = concatenation(l1,l2)
assert l3.valeur == 1
assert nieme_element(3, l3) == 4

l0 = None
l4 = concatenation(l1, l0)
l5 = concatenation(l0, l1)