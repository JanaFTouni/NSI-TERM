def tri_selection(lst: Cellule) -> None:
    """Procédure qui trie la liste lst dans l'ordre croissant"""
    courant = lst
    while courant is not None: 
        mini = courant
        reste = courant.suivante
        while reste is not None:
            if reste.valeur < mini.valeur:
                mini = reste
            reste = reste.suivante
        courant.valeur, mini.valeur = mini.valeur, courant.valeur
t        courant = courant.suivante

