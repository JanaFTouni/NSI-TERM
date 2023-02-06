# TRI PAR SELECTION

def echange(tab: list, i: int, j: int) -> None:
    """Procedure qui echange les elts du tableau d'indice i et j"""
    tmp = tab[i]
    tab[i] = tab[j]
    tab[j] = tmp
    
def tri_par_selection(tab:list) -> None:
    """Procedure qui trie le tableau tab ds lordre croissant"""
    for i in range(len(tab)):
        idx_min = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[idx_min]:
                idx_min = j
        echange(tab, i, idx_min)
    
#tests
t1 = [1,2,3]
echange(t1, 0, 1)
assert t1 ==[2, 1, 3]
t2 = [2,1,3]
tri_par_selection(t2)
assert t2 == [1,2,3]

# TRI PAR INSERTION

#efficacite
from time import perf_counter
from random import randint

def tableau_aleatoire(n: int) -> list:
    """Renvoie un tab d'entiers aleatoires de taille n"""
    tab = [randint(1,n) for _ in range(n)]
    return tab

nb_pts = 5
abscisses = [0] * nb_pts
ordonnees = [0] * nb_pts
taille = 1_000

for i in range(nb_pts):
    abscisses[i] = taille
    tableau = tableau_aleatoire(taille)
    
    debut = perf_counter()
    tri_par_selection(tableau)
    fin = perf_counter()
    ordonnees[i] = fin -debut
    
    taille *= 2

import matplotlib.pyplot as plt
    
plt.figure("complexite temporelle du tri selection")
plt.title("complexite du tri")
plt.xlabel("Taille n du tableau")
plt.ylabel("Temps d'execution (en s)")  
plt.plot(abscisses, ordonnees, 'bo')
plt.show()