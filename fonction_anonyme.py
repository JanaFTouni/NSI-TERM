def calcul(op: callable, tab:list):
    """Calcule tab[0] op tab[1] op... op tab[n-1]
    Le tableau est suppose non vide"""
    res = tab[0]
    for i in range(1, len(tab)):
        res = op(res, tab[i])
    return res

def somme(a, b):
    return a + b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a//b

t0 = [1, 2, 5, 3, 4]
assert calcul(somme, t0) == 15
assert calcul(multiplication, t0) == 120
assert calcul(lambda x,  y: x + y, t0) == 15
assert calcul(lambda x,  y: max(x,y), t0) == 5
assert calcul(lambda x,  y: min(x,y), t0) == 1
