import sqlite3 as sgbd

connexion = sgbd.connect("mediatheque.db")
curseur = connexion.execute("SELECT * FROM auteur")
for elt in curseur:
    print(elt[0])
connexion.close()