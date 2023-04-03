from tri_selection import tri
from tri_place_test import tableau_aleatoire
from time import perf_counter
import matplotlib.pyplot as plt

tab = tableau_aleatoire(5_000, -100, 100)
debut = perf_counter()
tri(tab)
fin = perf_counter()
#print(fin - debut)

abscisses = [0] * 6 
ordonnees = [0] * 6 
i = 0 

for k in range(10,16):
    n = 2 **k
    tab = tableau_aleatoire(n, -100, 100)
    debut = perf_counter()
    tri(tab)
    fin = perf_counter()
    ordonnees[i] = fin - debut
   # print(f"Pour n = {n}, le temps necessaire est {fin - debut} s ")
    i += 1
    
plt.figure("Complexite temporelle")
plt.title("Performance du tri")
plt.xlabel("Taille du tableau")
plt.ylabel("Temps d'execution (en s)")
plt.plot(abscisses, ordonnees)
plt.show()