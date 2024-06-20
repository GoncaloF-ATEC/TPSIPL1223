
"""

ver se uma lista num contem valores duplicados

"""


def ex1(lista: list):
    aux = set()

    for i in lista:
        if aux.__contains__(i):
            return True
        aux.add(i)

    return False



"""

tendo uma lista ordenada  encontre os dois valores da lista q a sua soma seja t_sum,
 pode assumir que:
    todos os valores da lista são inteiros e a lista nunca esta vazia 
    eixtem dois valores que somados sao t_sum
    apenas eixtem dois valores que somados sao t_sum
    
"""

def ex2(lista: list, t_sum: int):
    pass


"""

tendo uma lista não ordenada  encontre os dois valores da lista q a sua soma seja t_sum,
 pode assumir que:
    todos os valores da lista são inteiros e a lista nunca esta vazia 
    eixtem dois valores que somados sao t_sum
    apenas eixtem dois valores que somados sao t_sum


"""

def ex3(lista: list, t_sum: int):
    pass