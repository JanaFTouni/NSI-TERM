def syracuse(un):
    """Affiche les termes de un tant que un > 1.
    u0 entier > 1. """
    print(un)
    if un <= 1:
        return None
    else:
        if un % 2 == 0:
            syracuse(un//2)
        else:
            syracuse(3 * un + 1)
            
# EXERCICE 4          
  
def boucle(i, k):
    print(i, end=' ')
    if i > k:
        return None
    if i < k :
        boucle(i + 1, k)