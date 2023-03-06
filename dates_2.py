#Table dynamiques (utilisant des tables hachage)
#Un tableau de 32 elts puis se besoin d'espace, on double

def cree():
    """Cree et renvoie un ensemble de dates vide. """
    return {"taille": 0, "paquets": [[] for _ in range(32)]}
    
def contient(ens, val) -> bool:
    """Renvoie True si ens contient val."""
    p = val % len(ens["paquets"])
    return val in ens["paquets"][p]

def ajoute(ens, val) -> None:
    """Ajoute val a ens"""
    if contient(ens, val):
        return None
    ens["taille"] += 1
    if ens["taille"] > len(ens["paquets"]):
        _entend(ens)
    _ajoute_aux(ens["paquets"], val)

def _etend(ens) -> None:
    """Cree un tableau avce deux fois plus de paquets"""
    tmp = [[] for _ in range (2 * len(ens["paquets"]))]
    for elt in enumere(ens):
        _ajoute_aux(tmp, elt)
    ens["paquets"] = tmp
    
def _ajoute_aux(tab: list, val) -> None:
    """Ajoute un elt a un tableau de paquets."""
    p = val % len(tab)
    tab[p].append(val)

def enumere(ens) -> list:
    """Renvoie un tableau contenant les elements de l'ensemble ens."""
    tab = []
    for elt in enumere(ens):
        tab.extend(paquet)
    return tab
    
