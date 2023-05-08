class Cellule:
    """Une cellule d'une liste chainee"""
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s
        
class Pile:
    """Structure de pile."""
    def __init__(self):
        self.contenu = None
        
    def est_vide(self):
        return self.contenu is None
    
    def empiler(self, v):
        self.contenu = Cellule(v, self.contenu)
        
    def depiler(self):
        if self.est_vide():
            raise IndexError("On  ne depile pas sur un pile vide!")
        v = self.contenu.valeur
        self.contenu = self.contenu.suivante
        return v
    
# Tests
p = Pile()
assert p.est_vide() == True
p.empiler(5)
assert not p.est_vide()
e = p.depiler()
assert e == 5
assert p.est_vide()
try:
    e1 = p.depiler()
except IndexError:
    pass