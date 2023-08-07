class Noeud:
    """ Un noeud d'une arborescense"""
    def __init__(self, v, f: list):
        self.valeur = v
        self.fils = f
        
def parcours_prefixe(a: Noeud) -> None:
    """Affiche les elts de a dans un parcours prefixe."""
    print(a.valeur)
    for enfant in a.fils:
        parcours_prefixe(a.enfant)
        
        
def parcours_postfixe(a: Noeud) -> None:
    """Affiche les elts de a dans un parcours prefixe."""
    for enfant in a.fils:
        parcours_postfixe(a.enfant)
    print(a.valeur)
    

a0 = Noeud('A', [Noeud('B', [Noeud('D', [])]), 
                Noeud('C', [Noeud('E', []), 
                Noeud('F', [Noeud('H', [])]),
                Noeud('G', [])])])

parcours_postfixe(a0)