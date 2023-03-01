from contient_doublon import contient_doublon
from random import randint

cpt = 0
nb_sim = 100
for _ in range(nb_sim):
    classe = [randint(1, 366) for _ in range(23)]
    if contient_doublon(classe):
        cpt= 1
        
print(f"La frequence de classe avec, au moins, 2 eleves ayant leur anniversaire\
a la meme date est {round(cpt /nb_sim, 2)}")