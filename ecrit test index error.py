def ecrit(tab, i, val) -> None:
    if i < 0:
        raise IndexError("Indice negatif")
    tab[i] = val