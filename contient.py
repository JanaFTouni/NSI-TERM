from dates import cree, contient, ajoute

def contient_doublon(tab: list) -> bool:
    """Renvoie True si le tableau contient un doublon
    False sinon""" 
    ens = cree()
    for elt in tab:
        if contient(ens, elt):
            return True
        ajoute(ens, elt)
    return False
    
#Tests
assert contient_doublon([12, 14, 125, 124]) == False
assert contient_doublon([12, 14, 124, 124]) == True