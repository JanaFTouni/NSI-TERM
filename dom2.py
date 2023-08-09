import xml.dom.minidom as dom

doc = dom.parseString("<a></a>")

a = doc.childNodes[0]
b = doc.createElement("b")
a.appendChild(b)
c = doc.createElement("c")
b.appendChild(c)


with open('sortie.xml', 'w') as f:
    f.write(doc.toxml())



