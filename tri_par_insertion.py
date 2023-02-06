def insere(tab: list, i: int, val) -> None:
    """insere val dans tab[0...i[ suppose deja trie."""
    j = i
    while j > 0 and tab[j-1] > val:
        tab[j] = tab[j - 1]
        j-= 1
    tab[j] = val
     
def tri_par_insertion(tab: list) -> None:
    """Procédure qui trie le tableau tab dans l'ordre croissant"""
    for i in range(1, len(tab)):
        # invariant : tab[0..i[ est trié
        tmp = tab[i]
        insere(tab, i, tmp)
#tests
t2 = [2, 4, 3]
tri_par_insertion(t2)
assert t2 == [2,3,4]