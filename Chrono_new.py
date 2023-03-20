class Chrono :
    """Une classe pour representer un temps mesure en heures, minutes, secondes."""
    def __init__(self,h, m, s):
        self._temps = 3600 * h + 60 * m + s
        
    def __str__(self):
        h, m, s = self._conversion()
        return f"{h}h {m}min {s}sec"
    
    def avance(self,s):
        self._temps += s
    
    def __eq__(self, u):
        return self._temps == u._temps 
    
    def __lt__(self, u):
        return self._temps < u._temps
    
    def clone(self):
        h, m, s = self._conversion()
        return Chrono(h, m, s)
    
    def _conversion(self):
        s = self._temps
        return ( s// 3600, (s//60) % 60, s % 60)