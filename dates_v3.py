
def cree():
    """Cree et renvoie un ensemble de dates vide. """
    return [] 

def contient(ens, val) -> bool:
    """Renvoie True si ,et seulement si, l'ensemble ens contient la date val."""
    return (val in ens)

def ajoute(ens, val) -> None:
    """Ajoute l'element val a l'ensemble ens si 1<= x <= 366
    et leve un exception Value Error si non"""
    if val <= 1 or val >= 366:
        raise ValueError(f"date {val} invalide")
    ens.append(val)