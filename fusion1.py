# class Cellule:
#     """Une cellule d'une liste chainée"""
#     def __init__(self, v, s):
#         self.valeur = v
#         self.suivante = s
#          
#     def __repr__(self) -> str:
#         return f"({self.valeur}, {self.suivante})"
#     
# l0 = Cellule(3, Cellule(5, Cellule(1, None)))
# 
# 
# def coupe(lst: Cellule) -> (Cellule, Cellule):
#     """Separer une liste en deux listes ayant le meme nb delements, a un pres"""
#     l1, l2 = None, None
#     courant = lst
#     while courant is not None:
#         if cpt % 2 == 0:
#             l1, l2 = Cellule(courant.valeur, l2),l1
#         courant = courant.suivante
#     return l1, l2
# 
# def fusion(l1, l2) -> Cellule:
#     """Fusionne deux listes triees"""
#     if l1 is None:
#         return l2
#     if l2 is None:
#         return l1
#     if l1.valeur <= l2.valeur:
#         return Cellule(l1.valeur, fusion(l1.suivante, l2))
#     else :
#         return Cellule(l2.valeur, fusion(l1, l2.suivante))
#     
#     
# l3 = Cellule(3, Cellule(5, Cellule(15, None)))
# l4 = Cellule(8, (Cellule(11, None)))
# l5 = fusion(l3, l4)
# 
# def tri_fusion(lst: Cellule) -> Cellule:
#     """Trie une liste avec tri fusion >
#     renvoie une liste chainne contenant les elements de lst trie dans l'ordre croissant"""
#     if lst is None: 
#         return lst
#     if lst.suivante is None:
#         return lst
#     l1, l2 = coupe(lst)
#     return fusion(tri_fusion(l1), tri_fusion(l2))  
#     
# # def coupe(lst: Cellule) -> (Cellule, Cellule):
# #     """Separer une liste en deux listes ayant le meme nb delements, a un pres"""
# #     l1, l2 = None, None
# #     courant = lst
# #     cpt = 0
# #     while courant is not None:
# #         if cpt % 2 == 0:
# #             l1 = Cellule(courant.valeur, l1)
# #         else:
# #             l2 = Cellule(courant.valeur, l2)
# #         courant = courant.suivante
# #         cpt += 1
# #     return l1, l2    
# 
# import sys
# from random import randint
# 
# sys.setrecursionlimit(4_000)
# 
# l8  = None
# taille = 1_000
# for _ in range(taille):
#     nb = randint(0, taille)
#     l8 = Cellule(nb, l8)
#     
# l9 = tri_fusion(l8)