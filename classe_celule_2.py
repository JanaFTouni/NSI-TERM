class Cellule:
    """Une cellule d'une liste chaînée"""
    def __init__(self, val, s):
        self.valeur = val
        self.suivante = s
        
        
#iterative
def longueur(lst: Cellule) -> int:
    """Renvoie la longueur de la liste t """
    n = 0
    courant = lst
    while courant is not None :
        n += 1
        courant = courant.suivante
    return n

#recursive
def longueur(lst: Cellule) -> int:
    """Renvoie la longueur de la liste t """
    if lst is None:
        return 0
    else:
        return 1 + longueur(lst.suivante) 


l0 = None
assert longueur(l0) == 0
l1 = Cellule(5, None)
assert longueur(l1) == 1
l2 = Cellule(3,Cellule(5, Cellule(1, None)))
assert longueur(l2) == 3 