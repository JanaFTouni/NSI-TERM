def contient_doublon(tab: list) -> bool:
    """Renvoie True si le tableau contient un doublon
    False sinon""" 
    ens = [0] * 6
    for elt in tab:
        if ens[elt // 64] & (1 << (elt % 64)) != 0:
            return True
        ens[elt // 64] = ens[elt // 64] | (1 << (elt % 64))
    return False
    
#Tests
assert contient_doublon([12, 14, 125, 124]) == False
assert contient_doublon([12, 14, 124, 124]) == True