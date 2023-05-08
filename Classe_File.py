class Cellule:
    """Une cellule d'une liste chainee"""
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s
        
class File:
    """Structure de fille."""
    def __init__(self):
        self.tete = None
        self.queue = None
        
    def est_vide(self):
        return self.tete is None
    
    def ajouter(self, x):
        c = Cellule(x, None)
        if self.est_vide():
            self.tete = c
        else:
            self.queue.suivante = c
        self.queue = c
        
    def retirer(self):
        if self.est_vide():
            raise IndexError("On  ne depile pas sur un pile vide!")
        v = self.tete.valeur
        self.tete = self.tete.suivante
        if self.tete is None:
            self.queue = None
        return v
    
    
# Tests
f0 = File()
assert f0.est_vide()
f0.ajouter(2)
assert not f0.est_vide()
f0.ajouter(8)
f0.ajouter(9)
e0 = f0.retirer()
assert e0 == 2

            