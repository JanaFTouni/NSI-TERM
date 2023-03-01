def contient_doublon(tab: list) -> bool:
    """Renvoie True si le tableau contient un doublon
    False sinon""" 
    ens = [False] * 367
    for elt in tab:
        if ens[elt]:
            return True
        ens[elt] = True
    return False
    
#Tests
assert contient_doublon([12, 14, 125, 124]) == False
assert contient_doublon([12, 14, 12, 124]) == True