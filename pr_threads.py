import threading

def hello(n:int) -> None:
    for i in range(5):
        print(f"Je suis le thread {n} et ma valeur est {i}")
    print(f"------- FIn du thread {n}")
    
for n in range(4):
    t = threading.Thread(target= hello, args=[n])
    t.start()