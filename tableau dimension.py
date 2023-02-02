#Matrice en extension

t = [[1, 0, 0, 0, 0],
     [0, 0, 1, 0, 1],
     [0, 1, 0, 1, 0]]

#Matrice par compréhension
t2 = [[0] * 5 for _ in range(3)]

#somme des elt de t
for i in range(3):
    for j in range(5):
        s += t[i][j]

s = 0
for ligne in t:
    print(ligne)
    for elt in ligne:
        s += elt