"""
-b +- raiz(b^2 -4ac)/2a

"""
import math

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
    i = calc_int_raiz(a, b, c)

    # Condição de exclusão
    if div_zero(a) or ( i < 0 ):
        return False

    raiz = math.sqrt(i)

    x1 = (-b + raiz) / (a * 2)
    x2 = (-b - raiz) / (a * 2)

    print(f"x1: {x1}\nx2: {x2}")

fresolv(a, b, c)