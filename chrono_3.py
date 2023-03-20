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
        # depassement secondes
        self.minutes += self.secondes // 60
        self.secondes = self.secondes % 60
        #depassement minutes
        self.heures += self.minutes // 60
        self.minutes = self.minutes & 60
        
    def __str__(self): #methode special
        return self.texte()
    #     def __str__(self): #methode special
    #    return f"{self.heures}h {self.minutes}min {self.secondes}sec"