def insere(inf: callable , tab: list, i: int, val) -> None:
    """Procédure qui insère val dans tab[0..i[ supposé trié"""
    j = i
    while j > 0 and not inf(tab[j - 1], val):
        tab[j] = tab[j - 1]
        j = j - 1
    tab[j] = val
    
def tri(inf: callable ,tab: list) -> None:
    """Procédure qui trie le tableau tab dans l'ordre croissant
    pour la relation inf."""
    for i in range(1, len(tab)):
        tmp = tab[i]
        insere(inf, tab, i, tmp)
        
def inf1(x, y) -> bool:
    return x <= y

def inf2(x, y):
    return x[3] <= y[3]
    
    
t0 = [4, 5, 2, 7]
tri(inf1, t0)
assert t0 == [2, 4, 5, 7]
t1 = ["alors", "va", "ca"]
tri(inf1, t1)
assert t1 == ["alors", "ca", "va"]
t2 = [2.8, 1.4]
tri(inf1, t2)
assert t2 == [1.4, 2.8]
eleves = [("Brian", 1, 1, 1942), ("Grace", 9, 12, 1906), ("Linus", 28, 12,1969)]
tri(inf2, eleves)
assert eleves == [("Grace", 9, 12, 1906), ("Brian", 1, 1, 1942), ("Linus", 28, 12,1969)]
