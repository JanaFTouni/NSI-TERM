from os import getpid

pid = getpid()
with open("test.txt", 'w') as fichier:
    for i in range(1000):
        fichier.write(f"{pid} : {i}\n")
        fichier.flush() #vider le tampon de la sortie