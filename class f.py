class Noeud:
    """ Un noeud d'une arborescense"""
    def __init__(self, v, f: list):
        self.valeur = v
        self.fils = f

a0 = Noeud('A', [Noeud('B', [Noeud('D', [])]), 
                Noeud('C', [Noeud('E', []), 
                Noeud('F', [Noeud('H', [])]),
                Noeud('G', [])])])

def taille(a:Noeud) -> int:
    """Renvoie le nombre de Noeud de l'arbre a """
    a = 1
    for fils in a.fils:
        a += 1
        a = a.fils
    return a