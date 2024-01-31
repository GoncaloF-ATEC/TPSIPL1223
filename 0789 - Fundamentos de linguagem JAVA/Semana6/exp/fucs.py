"""

Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário.

Use uma função que receba um valor n inteiro imprima até a n-ésima linha.



I -> algo -> out

n -> valor inteiro

         1  2   3   4           Range
---------------------------
x = 1    1  _   _   _           range(1, 2) -> range(1, x+1)
x = 2    1  2   _   _           range(1, 3) -> range(1, x+1)
x = 3    1  2   3   _           range(1, 4) -> range(1, x+1)
x = 4    1  2   3    4


nl = nc
"""

def ex2(n: int):

    for x in range(1, n+1): # n <: m-1
        for y in range(1, x+1):
            print(f"{y}", end=" ")
        print("")


print(abs(-12))


"""
print("teste") -> teste\n




"""

"""
1 
1 2 
1 2 3 


"""