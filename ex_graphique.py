from classe_Noeud import Noeud

# a3 = Noeud(Noeud(Noeud(None, "A", None),"B", Noeud(Noeud(None, "C", None),"D",Noeud(None, "E", None))) ,"F", Noeud(None, "G", Noeud(Noeud(None, "H", None),"I", None)))
# a3.show()


f1 = Noeud(None, 'C', None)
n1 = Noeud(None, 'B', f1)
f2 = Noeud(None, 'D', None)
a1 = Noeud(n1, 'A', f2)
a1.show()