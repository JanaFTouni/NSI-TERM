import sqlite3 as sgbd

connexion = sgbd.connect("mediatheque.db")
prenom = input("Prenom recherche : ")
curseur = connexion.execute(f"""SELECT nom, prenom
                            FROM auteur
                            WHERE upper(prenom) = upper(?)
                            ORDER BY nom;""", (prenom,))
for elt in curseur:
    print(elt)
connexion.close()