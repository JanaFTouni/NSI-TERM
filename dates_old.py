def cree():
    """Crée et renvoie un ensemble de dates vide."""
    return [0] * 6

def contient(ens, val) -> bool:
    """Renvoie True si ens contient val."""
    if val < 1 or val > 366:
        return False
    paquet = val // 64
    bit = val % 64
    return (ens[paquet] & (1 << bit)) != 0
    

def ajoute(ens, val) -> None:
    """Ajoute val à ens et leve une exception si val nest pas valide."""
    if val < 1 or val > 366:
        raise ValueError(f"date{val} invalide")
    paquet = val // 64
    bit = val % 64
    ens[paquet] = (ens[paquet] | (1 << bit))