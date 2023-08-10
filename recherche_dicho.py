def recherche(tab: list, val, g:int,  d:int) -> int|None:
    """Renvoie une position de val dans le tab[g...d],
    suposse trie, et None si val ne sy trouve pas """
    if g > d:
        return None
    m = (g + d) //2
    if tab[val] > tab[m] :
        return recherche(tab, val ,m + 1, d) 
    elif tab[val] < tab[m]:
        return recherche(tab, val ,g, m - 1)
    else: 
        return m
    
def recherche_dichotomique(tab: list, val) -> int|None :
    return recherche(tab, val, 0, len(tab) - 1)
