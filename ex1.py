import sqlite3 as sgbd

# connexion a la base
connexion  = sgbd.connect("mediatheque.db")
#suppresion eventuelle de l'ancienne table
connexion.execute("DROP TABLE IF EXISTS auteur")
# creation de la table auteur
connexion.execute("""CREATE TABLE AUTEUR(
                    id INT PRIMARY KEY,
                    nom VARCHAR(90) NOT NULL,
                    prenom VARCHAR(90) NOT NULL
                    );""")

# validation
connexion.commit()

# deconnexion
connexion.close()