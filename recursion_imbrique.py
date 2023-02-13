def f91(n: int) -> int :
    if n > 100:
        return n - 10
    if n <= 100:
        return f91(f91(n + 11 ))
    
    
assert f91(99) == 91

def a(n: int) -> int:
    if n == 0 :
        return 1
    else:
        return n - b(a(n-1))
    
    
def b(n: int) -> int:
    if n == 0 :
        return 0
    else:
        return n - a(b(n-1))

assert a(0) == 1
assert a(1) == 1
assert a(2) == 2
assert a(3) == 2
assert b(0) == 0
assert b(1) == 0
assert b(2) == 1
assert b(3) == 2