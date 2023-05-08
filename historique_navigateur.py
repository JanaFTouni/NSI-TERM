adresses_precedentes = creer_pile()
adresse_courante = ""

def aller_(adresse_cible):
    global adresse_courante
    empiler(adresses_precedentes, adresse_courante)
    adresse_courante = adresse_cible
    
def retour():
    global adresse_courante
    if not est_vide(adresses_precedents):
        adresse_courante = depiler(adresse_precedentes)
        
