def derive(f: callable, h: float= 1e-7) -> callable:
    """Renvoie une fonction qui approche la dérivée de la fonction f."""
    return lambda x: (f(x+h) - f(x)) / h

def carre(x):
    return x**2

d = derive(carre, 1e-10)