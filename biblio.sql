CREATE TABLE IF NOT EXISTS usager ( 
	nom VARCHAR(90),
	prenom VARCHAR(90),
	adresse VARCHAR(300),
	cp VARCHAR(5), 
	ville VARCHAR(60),
	email VARCHAR(60),
	code_barre CHAR(15) PRIMARY KEY
	);
	
CREATE TABLE IF NOT EXISTS livre(
	titre VARCHAR(300),
	editeur VARCHAR(90),
	annee INT,
	isbn CHAR(14) PRIMARY KEY
	);

CREATE  TABLE IF NOT EXISTS auteur(
	nom VARCHAR(300),
	prenom VARCHAR(90),
	a_id INT PRIMARY KEY
	);
	
CREATE TABLE IF NOT EXISTS auteur_de(
	a_id INT REFERENCES auteur(a_id),
		isbn CHAR(14) REFERENCES livre(isbn),
		PRIMARY KEY (a_id, isbn)
		);
	
CREATE TABLE IF NOT EXISTS emprunt(
	code_barre CHAR(15) REFERENCES usager(code_barre),
	isbn CHAR(15) PRIMARY KEY REFERENCES livre(isbn),
	retour DATE);

