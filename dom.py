import xml.dom.minidom as dom

with open ("recette.xml") as f:
    doc2 = dom.parse(f)

doc3 = dom.parseString("<a> mon jole<b>document</b></a>")

def taille(a: dom.Document) -> int:
    """Renvoie le nombre de Noeud de l'arbre a """
    t = 1
    for enfant in a.childNodes:
        t += taille(enfant)
    return t




