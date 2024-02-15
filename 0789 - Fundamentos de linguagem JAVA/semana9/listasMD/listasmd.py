lista = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]



# lista[linha][coluna]

print(lista[0][0])
print(lista[1][1])
print(lista[2][0])


for linha in lista:
    print(linha)


for linha in lista:
   for elemento in linha:
       print(elemento)


lista[0].append([99,23]) # add a lista

print(lista)
lista[1].extend([99,23]) # add o conteudo da lista
print(lista)