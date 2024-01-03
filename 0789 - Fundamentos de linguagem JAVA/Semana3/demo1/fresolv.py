"""
-b +- raiz(b^2 -4ac)/2a

"""

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))


def div_zero(a: float):
    if a == 0.0:
        return True

    return False

def calc_int_raiz(a: float, b: float, c:float):
    #raiz(b^2 -4ac)
    int_raiz = (b * b) - (4 * a * c)
    if int_raiz >= 0.0:
        return int_raiz
    else:
        return False

def fresolv(a:float, b:float, c:float):
    i = b #calc_int_raiz(a, b, c)

    # Condição de exclusão
    if div_zero(a) or ( i < 0 ):
        return False

    return True



print(fresolv(-1, -1, 2))

print(fresolv(-1, 0, 2))

print(fresolv(-1, 1, 2))


print(fresolv(0, -1, 2))

print(fresolv(0, 0, 2))

print(fresolv(0, 1, 2))

print(fresolv(9, -1, 2))

print(fresolv(9, 0, 2))

print(fresolv(9, 1, 2))

