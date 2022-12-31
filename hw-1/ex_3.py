def amulet_area(a, b, c):
    p = (a + b + c) / 2
    import math
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return S
    
assert amulet_area(3, 4, 5) == 6
