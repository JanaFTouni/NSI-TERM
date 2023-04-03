class Cellule:
    """Une cellule d'une liste chaînée"""
    def __init__(self, val, s):
        self.valeur = val
        self.suivante = s
        
        
# CONSOLE
# c0 = Cellule(1, None)
# c1 = Cellule(5, c0)
# c2 = Cellule(3, c1)
lst = Cellule(3,Cellule(5, Cellule(1, None)))

from random import randint 


taille = 10
lst = None # liste vide
for _ in range(taille):
    val = randint(0,100)
    lst = Cellule(val, lst)

for i in range(taille):
    print(lst.valeur, end =' ')
    lst = lst.suivante

