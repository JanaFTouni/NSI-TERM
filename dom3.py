import xml.dom.minidom as dom

doc = dom.parseString("<a></a>")

a = doc.childNodes[0]
b = doc.createElement("b")
b.setAttribute("quantite", "10")
d = doc.createTextNode("contenu")
c = doc.createElement("c")
a.appendChild(b)
b.appendChild(d)
a.appendChild(c)


with open('sortie2.xml', 'w') as f:
    f.write(doc.toxml())
    