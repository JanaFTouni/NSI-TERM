def monnaie(somme: int, systeme: list) -> int:
    """renvoi le nb de devises minimal pour obtenir la somme.
    systeme : tb trié qui represente le system monitaire."""
    i  =len(systeme) - 1
    nb_devises = 0
    while somme > 0:
        if somme >= systeme[i]:
            somme -= systeme[i]
            nb_devises += 1
        else:
            i -= 1
    return nb_devises

euros = [1, 2, 5, 10, 20, 50, 100]
assert monnaie(9, euros) == 3
assert monnaie(3, euros) == 2
print("Les test sont passés...")

#pas_ok = [1,3,4]
#assert monnaie(6, pas_ok) == 2