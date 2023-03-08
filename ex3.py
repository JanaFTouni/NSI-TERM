import dates

ens = dates.cree()

while True:
    try:
        date = int(input("Entrer un jour : "))
        dates.ajoute(ens, date)
        break
    except ValueError:
        print("Il faut mettre un entier comppris entre 1 et 366")
    
    


