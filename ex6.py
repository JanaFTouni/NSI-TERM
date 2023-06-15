from class_ABR import ABR

a = ABR()
a.ajouter(3)
assert not a.contient(1)
a.ajouter(1)
assert a.contient(1)
a.ajouter(4)
a.ajouter(2)
