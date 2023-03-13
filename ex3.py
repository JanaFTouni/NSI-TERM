import sqlite3 as sgbd

# connexion a la base
connexion  = sgbd.connect("mediatheque.db")
liste_auteurs = [(103, 'Toriyama', 'Akira'),
                 (200, 'Rousseau', 'Jean Jacques')]
connexion.executemany("INSERT INTO auteur VALUES (?,?,?)", liste_auteurs)
connexion.commit()
connexion.close()