from random import randint

def d20 () -> int:
    return randint(1, 20)

def d6 () -> int:
    return randint(1, 6)

def xd6(count) -> int:
    res = 0
    for i in range(count):
        res += d6()
    
    return res

def xd20(count) -> int:
    res = 0
    for i in range(count):
        res += d20()
    
    return res
