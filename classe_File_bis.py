from classe_Pile import Pile

class File:
    """Structure de file."""
    def _init_(self):
        self.entree = Pile()
        self.sortie = Pile()
        
    def est_vide(self) -> bool:
        return self.entree.est_vide() and self.sortie.est_vide()
    
    def ajouter():
        self.entree.empiler(x)
        
    def retirer(self):
        if self.sortie.est_vide():
            while not self.entree.est_vide():
                cellule = self.entree.depiler()
                self.sortie.empiller(cellule)
        if self.sortie.est_vide():
            raise IndexError("On ne peut pas retirer dans une fille vide.")
        return self.sortie.depiler()
    
# # Tests
# f0 = File()
# assert f0.est_vide()
# f0.ajouter(2)
# assert not f0.est_vide()
# f0.ajouter(8)
# f0.ajouter(9)
# e0 = f0.retirer()
# assert e0 == 2
