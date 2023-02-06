from random import randint

def recherche_dichotomique(tab: list, val) -> None:
    """Renvoie un position de val dans le tab, suppose trie,
    et None si val ne s'y trouve pas """
    g = 0
    d = len(tab) - 1
    while g <= d:
        m = (g + d) // 2
        if tab[m] < val:
            g = m + 1
        elif tab[m] > val:
            d = m - 1
        else :
            return m
    return None
    
#Tests
taille  = 50
tableau = [randint(1, taille) for _ in range(taille)]
tableau.sort()
print(f"Tableau : {tableau}")
valeur = randint(1, taille)
print(f"Valeur : {valeur}")
print(recherche_dichotomique(tableau, valeur))