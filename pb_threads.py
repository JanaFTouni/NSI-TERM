import threading

verrou = threading.Lock()
compteur = 0

def incrc():
    global compteur
    for _ in range(100_000):
        verrou.acquire()
        v = compteur    #section critique // l.8 l.9 
        compteur = v + 1
        verrou.release()
        
th = []
for n in range(4):
    t = threading.Thread(target= incrc, args=[])
    t.start()
    th.append(t)
    
for t in th:
    t.join()
    
print(f"Valeur finale : {compteur}")