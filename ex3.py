class Noeud:
    """Un noeud d'un arbre binaire"""
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d

    def __str__(self):
        return f"({self.gauche}, {self.valeur}, {self.droit})"
    
a0 = Noeud(Noeud(None ,'A',Noeud(None, 'B', None)), 'C',Noeud(None, 'D', None))
a1 = Noeud(Noeud(Noeud(Noeud(None,"B",None),"C",Noeud(None, "E", None)),"F",None),"I",Noeud(Noeud(None,"J",Noeud(None,"S",None)),"T",None))

def minimum(a: Noeud):
    """Renvoie le plus petit element de l'ABR a.
    Si lárbre a est vide, alors cette fonction renvoie None"""
    if a is None:
        return None
    elif a.gauche is None:
        return a.valeur
    else:
        return minimum(a.gauche)
    
#tests
assert minimum(a0) == 'A'
assert minimum(a1) == 'B'

def supprime_minimum(a: Noeud) -> Noeud:
    """Supprime le plus petit element de a suposse non vide."""
    if a.gauche is None:
        return a.droit()
    else :
        return Noeud(supprime_minimum(a.gauche), a.valeur, a.droit)
    
#tests
a2 = supprime_minimum(a0)
a0.show()