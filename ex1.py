class Chrono:
    """Une classe pour representer un temps mesure en heures, minutes, secondes."""
    heure_max = 24 #Attribut de classe
    #initialiseur
    def __init__(self, h, m, s):
        self.heures = h #attributs d'instance
        self.minutes = m
        self.secondes = s
        
    def texte(self):
        return f"{self.heures}h {self.minutes}min {self.secondes}sec"
    
    def avance(self,s):
        self.secondes += s 