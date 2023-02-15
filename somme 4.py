
def somme(n: int) -> int:
    """Renvoie la somme des n premiers non nuls"""
    if n == 0:
        return 0
    else:
        return n + somme(n - 1)
    
assert somme(0) == 0
assert somme(1) == 1
assert somme(2) == 3
assert somme(5) == 15