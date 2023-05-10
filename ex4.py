class Cellule:
    """Une cellule d'une liste chainee"""
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s
        
class Pile:
    """Structure de pile."""
    def __init__(self):
        self.contenu = None
        self.longueur  = 0
        
    def est_vide(self):
        return self.contenu is None
    
    def empiler(self, v):
        self.contenu = Cellule(v, self.contenu)
        self.longueur  += 1 
        
    def depiler(self):
        if self.est_vide():
            raise IndexError("On  ne depile pas sur un pile vide!")
        v = self.contenu.valeur
        self.contenu = self.contenu.suivante
        self.longueur -= 1
        return v
    
    def consulter(self):
        if self.est_vide():
            raise IndexError("On  ne depile pas sur un pile vide!")
        return self.contenu.valeur 
        
    def vider(self):
        while not self.est_vide():
            self.depiler()
    
    def taille(self):
        return self.longueur
            
#Tests    
p = Pile()
assert p.est_vide() == True
p.empiler(5)
assert not p.est_vide()
e = p.depiler()
assert e == 5
p.empiler(4)
p.empiler(6)
assert p.taille() == 2
p.vider()
assert p.est_vide() == True


