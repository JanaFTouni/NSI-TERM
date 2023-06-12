import dis

code = """
v = compteur
compteur = v + 1
"""

dis.dis(code)
