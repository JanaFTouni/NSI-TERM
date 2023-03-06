#Table de Hachage
#Un tableau de 23 tableaux

def cree():
    """Cree et renvoie un ensemble de dates vide. """
    return [[] for _ in range(23)]

def contient(ens, val) -> bool:
    """Renvoie True si ens contient val."""
    return val in ens[val % 23]

def ajoute(ens, val) -> None:
    """Ajoute val a ens"""
    ens[val % 23].append(val)
    
def enumere(ens) -> list:
    """Renvoie un tableau contenant les elements de lensemble ens."""
    tab = []
    for paquet in ens:
        for elt in paquet:
            tab.append(elt)
    return tab

#Tests
e0 = [[46, 92],[1,47],[],[],[], [],[],[],[],[],[],[],[],[],[],[22],[],[],[],[],[],[],[]]
assert enumere(e0) == [46,92,1,47,22]