def calcul(f: callable, op: callable, tab: list):
    res = f(tab[0])
    for i in range(1, len(tab)):
        res = op(res, f(tab[i]))
    return res
   
#Tests
assert calcul(lambda x: 2*x, lambda a,b: a+b, [1,2,3]) == 12

t = [1,2,3,4]
assert calcul(lambda x: str(x), lambda x, y: x + ", "+ y, t) == "1, 2, 3, 4"
assert calcul(lambda i: str(2*i), lambda x, y: x + ", "+ y, t) == "2, 4, 6, 8"
 
