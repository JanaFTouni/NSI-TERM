def cree():
    """Cree et renvoie un ensemble de dates vide. """
    return [0] * 6

def contient(ens, val) -> bool:
    """Renvoie True si ens contient val."""
    paquet = val // 64
    bit = val % 64
    return (ens[paquet] & (1 << bit)) != 0

def ajoute(ens, val) -> None:
    """Ajoute val a ens"""
    paquet = val // 64
    bit = val % 64
    ens[paquet] = (ens[paquet] | (1 << bit))