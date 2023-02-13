#RECURSIVITE

def somme(n: int) -> int:
    """Renvoie la somme des n premiers non nuls"""
    assert n >= 0 , "N doit etre un entier naturel"
    if n == 0:
        return 0
    else:
        return n + somme(n - 1)
