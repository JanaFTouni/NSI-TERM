# Construction en extension
t = [2, 3, 4]

#parcours (avec indice)

for i in range(len(t)):
    print(t[i])
    
def moy (tab: list) -> float: #float: division 
    """Renvoi la moyenne des elts de tab"""
    acc =0
    for i in range(len(t)):
        acc = acc + tab[i]
    return acc / len(tab)
    
#parcours (sans indice)
for elt in t:
    print(elt)
          
def moy (tab: list) -> float:
    """Renvoi la moyenne des elts de tab"""
    acc =0
    for elt in tab:
        acc += elt 
    return acc / len(tab)

assert moy(t) == 3.0s

t = [''] * 10
t[0] = "hello"

t2 = [0] * 100
for i in range(100):
    t2[i] = i * i

u = [0] * len(t2)
for i in range(len(u)):
    u[i] = t2[i]
    
# Construction par compréhension

t3 = [i*i for i in range(100)]
    