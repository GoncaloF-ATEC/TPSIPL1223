"""
var

"""
"""
idade: int = 10

soma = idade + 10
print(soma)


soma = 10 + 2

calc = soma * 5 # (10 + 2) * 5
print(calc)


print(10/5)
print(10//5)

print(10 / 3)

print(10 // 3)

print(10 % 3)


print(327 % 42)

"""
"""

if

"""

numero = int(input('Digite um numero: '))


if numero % 2 == 0: # se
    print('O numero é par')
elif numero % 5 == 0: # senao se
    print('o não é par mas é div por 5')
elif numero % 3 == 0: # senao se
    print('o numero nao e par, nem div por 5 mas e div por 3')
else: # senao
    print('o numero não e par')

"""
match

"""

nota = 42
match nota:
    case 10:
        print("nota 10")
    case 15:
        print("nota 15")
    case _:
        print("outra nota")


print("--" * 10)

if numero % 2 == 0 and (numero % 5 == 0 or numero == 42):
    print('O numero é par e div por 5 ou 42')


if numero == 0:
    pass

print("--" * 10)


def ola_mundo():
    print("Ola Mundo")


ola_mundo()
ola_mundo()
ola_mundo()
print("--" * 10)

def ola_mundo2(nome: str):
    print(f"Ola Mundo, {nome}")


ola_mundo2("Joao")
ola_mundo2("Maria")
ola_mundo2("Rita")
ola_mundo2(30)

print("--" * 10)


def ola_mundo3(nome: str) -> str:
    return f"Ola Mundo, {nome}"

n1 = ola_mundo3("Joao") # f"Ola Mundo, Joao"
n2 = ola_mundo3("Maria") # f"Ola Mundo, Maria"
n3 = ola_mundo3("Rita") # f"Ola Mundo, Rita"


print(n1)
print(ola_mundo3("Rita"))


print("--" * 10)


if not 0:
    print("ok")