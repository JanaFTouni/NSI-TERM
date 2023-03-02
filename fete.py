from dates import cree, contient, ajoute
from random import randint

def fete_continue() -> int:
    """Renvoie le nombre d'eleves minimal pour qu'il y ait des anniversaires
    tous les jour"""
    compteur = 0
    nombre_dates = 0
    ensemble = cree()
    while nombre_dates < 366:
        compteur += 1
        date = randint(1, 366)
        if not contient(ensemble, date):
            nombre_dates += 1
            ajoute(ensemble, date)
    return compteur

nb_sim = 1000
somme = 0
for _ in range(nb_sim):
    somme += fete_continue()
print(f"En moyenne, il faut {somme/ nb_sim}")