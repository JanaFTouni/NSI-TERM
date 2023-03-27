import sqlite3 as sgbd

connexion = sgbd.connect("mediatheque.db")
name = input("Nom recherche : ")
curseur = connexion.execute(f"SELECT * FROM auteur WHERE nom = '{name}' ")
for elt in curseur:
    print(elt)
connexion.close()