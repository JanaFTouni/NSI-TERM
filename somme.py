def somme(n: int) -> int :
    """Renvoie la somme des n premiers entiers"""
    a = 0
    for i in range(0, n + 1):
        a += i
    return a 
        
assert somme(0) == 0
assert somme(1) == 1
assert somme(2) == 3
assert somme(5) == 15

#RECURSIVITE

def somme(n: int) -> int:
    """Renvoie la somme des n premiers non nuls"""
    if n == 0:
        return 0
    else:
        return n + somme(n - 1)