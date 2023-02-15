#RECURSIVITE

def somme(n: int) -> int:
    """Renvoie la somme des n premiers non nuls"""
    assert n >= 0 , "N doit etre un entier naturel"
    if n == 0:
        return 0
    else:
        return somme_bis(n)

def somme_bis(n: int) -> int:
    """Renvoie la somme des n premiers naturels non nuls"""
    assert n >= 0, "n doit etre un entier naturel"
    if n == 0:
        return 0
    else:
        return n + somme_bis(n -1)
    
assert somme(0) == 0
assert somme(1) == 1
assert somme(2) == 3
assert somme(5) == 15