def rebours(n:int ) -> None:
    if n < 0:
        return None
    else:
        print(n)
        rebours(n - 1)
        
def compte(n:int ) -> None:
    if n < 0:
        return None
    else:
        compte(n - 1)
        print(n)