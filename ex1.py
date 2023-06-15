from classe_Noeud import Noeud
        
a0 = Noeud(Noeud(None ,'A',Noeud(None, 'B', None)), 'C',Noeud(None, 'D', None))
a1 = Noeud(Noeud(Noeud(Noeud(None,"B",None),"C",Noeud(None, "E", None)),"F",None),"I",Noeud(Noeud(None,"J",Noeud(None,"S",None)),"T",None))

#ABR structure mutable
def ajoute(x, a: Noeud) -> Noeud :
    """Modifie l'ABR a en lui ajoutant un elt x"""
    pass

#ABR structure immuable
def ajoute(x, a: Noeud) -> Noeud :
    """Ajoute x a l'arbre a, renvoie un nouvel arbre"""
    if a is None:
        return Noeud(None, x, None)
    else :
        if x < a.valeur:
            return Noeud(ajoute(x, a.gauche), a.valeur, a.droit)
        else:
            return Noeud(a.gauche, a.valeur, ajoute(x, a.droit))
        
a2 = ajoute('L', a1)
#a2.show()
        
a = ajoute(1, None)
a = ajoute(4, a)
a = ajoute(3, a)
a.show()

def taille(a: Noeud) -> int:
    """Renvoie le nombre de noeuds de l'arbre a"""
    if a is None:
        return 0
    else:
        return 1 + taille(a.gauche) + taille(a.droit)
assert taille(a0) == 4
assert taille(a1) == 8 

def hauteur(a: Noeud) -> int:
    """Renvoie la hauteur de l'arbre a"""
    if a is None:
        return 0
    else:
        return 1 + max(hauteur(a.gauche), hauteur(a.droit))
    
assert hauteur(a0) == 3
assert hauteur(a1) == 4

def parcours_infixe(a: Noeud) -> None:
    if a is None:
        return None
    else :
        parcours_infixe(a.gauche)
        print(a.valeur)
        parcours_infixe(a.droit)
        
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
        
assert appartient('A', a0) == True 
assert appartient('B', a0) == True
assert appartient('Z', a0) == False
assert appartient('Z', a1) == False
assert appartient('E', a1) == True