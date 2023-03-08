def cree():
    """Crée et renvoie un ensemble de dates vide"""
    return [0]

def contient(ens, val) -> bool:
    """Renvoie True si, et seulement si, l'ensemble ens contient la date val"""
    return(ens[0] &(1 << val) != 0)
    
def ajoute(ens, val) -> None:
    """Ajoute l'élément val à l'ensemble ens si 1 <= x <= 366 
    et lève une exception ValueError sinon"""
    ens[0] = ens[0] | (1 << elt)