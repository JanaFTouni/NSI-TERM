from tri_selection import tri
from random import randint


def occurrences(tab: list) -> dict:
    """Renvoie le dictionnaire des occurrences de tab"""
    dico = {}
    for elt in tab:
        if elt in dico:
            dico[elt] += 1
        else:
            dico[elt] = 1
    return dico

assert occurrences([5,4,5,6]) == {5: 2, 4: 1, 6: 1}

def identiques(d1: dict, d2: dict) -> None:
    """Vérifie si deux dictionnaires sont identiques"""
    for cle in d1:
        assert cle in d2
        assert d1[cle] == d2[cle]
    for cle in d2:
        assert cle in d1
        assert d2[cle] == d1[cle]
        

def test(tab: list) -> None:
    """Teste la fonction tri sur le tableau tab"""
    d1 = occurrences(tab)
    tri(tab)
    for i in range(0, len(tab) - 1):
        assert tab[i] <= tab[i + 1]
    identiques(d1, occurrences(tab))
        
test([])
test([1])
test([2,1])

def tableau_aleatoire(n:int, a:int, b:int) -> list:
    """Renvoie un tableau de taille n.
    les elts son generes aleatoirement entre a et b """
    return [randint(a,b) for _ in range(n)]
