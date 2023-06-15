from classe_Noeud import Noeud
        
    
def supprime(x, a) -> Noeud:
    """Supprime une ocurrence de x dans a """
    if a is None :
        return None
    else :
        if x < a.valeur:
            return Noeud(supprime(x, a.gauche), a.valeur, a.droit)
        elif x > a.valeur:
            return Noeud(a.gauche, a.valeur, supprime(x, a.droit))
        elif a.droit is None :
            return a.gauche
        else :
            return Noeud(a.gauche minimum(a.droit), supprime_minimum(a.droit))
        

def appartient(x, a: Noeud) -> bool:
    """Determine si x appartient dans l'ABR a."""
    if a == None:
        return False
    else:
        if a.valeur == x:
            return True 
        elif x < a.valeur:
            return appartient(x, a.gauche)
        else:
            return appartient(x, a.droit)
        

class ABR:
    """Un arbre binaire de recherche."""
    def __init__(self):
        self.racine = None
        
    def ajouter(self, x):
        self.racine = ajoute(x, self.racine)
    
    def contient(self, x):
        return appartient(x, self.racine)
    
    