tab = [1 , 1, 2, 3, 5, 8, 13]
val = 4


# tab.insert(0, val) :
tab.append(None)
for i in range(len(tab) -1, 0, -1):
    tab[i] = tab[i - 1]
tab[0] = val

tab.pop()



