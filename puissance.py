def puissance(x, n) -> int:
    """Renvoie x*n
n entier naturel """
    if n == 0:
        return 1
    else:
        return x * puissance(x,n-1)
     
    
assert puissance(2,0) == 1
assert puissance(2,3) == 8
assert puissance(-2,3) == -8
assert puissance(-2,4) == 16