class Pile:
    """Structure de pile."""
    def __init__(self):
        self.contenu = []
        
    def est_vide(self):
        return len(self.contenu) == 0
    
    def empiler(self, v):
        self.contenu.append(v)
    
    def depiler(self):
        if self.est_vide():
            raise IndexError("On  ne depile pas sur un pile vide!")
        return self.contenu.pop()
    
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