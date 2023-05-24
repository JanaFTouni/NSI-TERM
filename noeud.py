class Noeud:
    """Un noeud dun arbre binaire"""
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d


def taille(a: Noeud) -> int:
    """Renvoi le nombre de noeuds de l'arbre a. """
    if a is None :
        return 0
    else:
        return 1 + taille(a.gauche) + taille(a.droit)
    
def hauteur(a: Noeud) -> int:
    """Renvoie la hauteur de l'arbre a"""
    if a is None:
        return 0
    else:
        return 1 + max(hauteur(a.gauche), hauteur(a.droit))
        
def parcours_prefixe(a: Noeud) -> None:
    """Affiche les éléments de a dans un parcours prefixe."""
    if a is None:
        return None
    else:
        print(a.valeur)
        parcours_prefixe(a.gauche)
        parcours_prefixe(a.droit)
        
def parcours_infixe(a) :
    if a is None :
        return None
    else :
        parcours_infixe(a.gauche)
        print(a.valeur)
        parcours_infixe(a.droit)

     
def parcours_postfixe(a) :
    if a is None :
        return None
    else :
        parcours_postfixe(a.gauche)
        parcours_postfixe(a.droit)
        print(a.valeur)
    

# ex 3
def affiche(a) :
    if a is None :
        return None
    else :
        print('(',end = '')
        affiche(a.gauche)
        print (f"{a.valeur}", end ='')
        affiche(a.droit)
        print(')', end = '')



a0 = Noeud(Noeud(None, "B",  Noeud(None, "C", None)), 'A', Noeud(None, "D", None))
assert taille(a0) == 4
a1 = None
assert taille(a1) == 0
a2 = Noeud(None, 'A', None)
assert taille(a2) == 1
assert taille(a0) == 4
a3 = Noeud(Noeud(Noeud(None, "A", None),"B", Noeud(Noeud(None, "C", None),"D",Noeud(None, "E", None))) ,"F", Noeud(None, "G", Noeud(Noeud(None, "H", None),"I", None)))