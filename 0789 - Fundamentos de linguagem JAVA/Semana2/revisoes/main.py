# cira var

nome = "Carlos"
idade = 20
ano_curr = 2023

# print

print(f"o {nome} tem {idade} anos")

# op com variaveis

"""

+
-
/
*

% - modulo <- resto da div inteira
// <- div inteira

6 / 2 = 3, resto 0  -> 3
6 % 2 = 3, resto 0  -> 0

5 / 2 = 2, resto 0  -> 2,5
5 // 2 = 2, resto 0  -> 2

5 % 2 = 3, resto 0  -> 1


** <- elevado
"""

a = 6
b = 2
print(a + b)
print(a - b)
print(b - a)
print(a * b)
print(a / b) # <- 3.0
print(a // b) # <- 3
print(a % b) # <-0

print("--"*10)
a = 5
b = 2
print(a / b) # 2.5
print(a // b) # 2
print(a % b) # 1

print("--"*10) # <- separador

a = 3
b = 2
print(b ** a) # <- 8

print("--"*10) # <- separador
# input

nome_input = input("qual o seu nome: ")
idade_input = input("qual o sua idade: ")

print(f"O nome inserido foi {nome_input} e tem {idade_input} anos")

# converter tipos de dados

idade_input_int = int(idade_input) # novoTipo(valor)
ano_int = int("2023")
ano_nasc = ano_int - idade_input_int

print(f"O nome inserido foi {nome_input} e tem {idade_input} anos e nasceu em {ano_nasc}")

# condições

"""

>  <- 30 > 3 -> True  ||  30 > 34 -> False
<
>=
<=
== 
!=

not Cond

Cond and Cond <- e
Cond or Cond <- ou

"""
numA = 10
numB = 15
numC = 20

if not (numA < numB): # numA > numB
    print("True")
elif numA > numB or numC > numA: # else if
    print("False")
else:
    print("else")




print("foro do bloco")


#    print("dentro do bloco") <- erro