from Pessoa import Pessoa

p1 = Pessoa("Carlos", 20, "Masc")
print(p1)
print(p1.nome)
p1.nome = "Mário"
print(p1.nome)
print(p1)

p2 = Pessoa("Maria", 40, "Fem")
print(p2.nome)
print("--" * 10)
print("--" * 10)
p3 = p1
print(p3)
print(p1)

p3.nome = "Paulo"
print("--" * 10)
print("--" * 10)

print(p3)
print(p1)


num = 109
print(num)
print(num.bit_count())
print(num)


num = 123

num2 = num

num2 = 1
print(num)

l = [1,2,3,4]
print(l)
l.append(10)
print(l)



nome = "goncalo"

print(nome.capitalize())

#nome[3] = "w"

for i in nome:
    print(i)

print("--" * 10)
print("--" * 10)
print("--" * 10)
print("--" * 10)


def mudar_nome(novo_nome: str, pessoa: Pessoa):
    pessoa.nome = novo_nome

def mudar_num(num12: int, num2: int):
    num12 = num2
    return num12

print(p1.nome)

mudar_nome("Rui", p1)

print(p1.nome)


print("--" * 10)
print("--" * 10)
print("--" * 10)
a = 10
b = 20

mudar_num(a,b)

print(a)
print(b)
print("--" * 10)
print("--" * 10)
print("--" * 10)

print(p1.idade)
print(p2.idade)
p1.envelhecer(10)
print(p1.idade)
print(p2.idade)

p1.envelhecer() #  p1.envelhecer(1)
print(p1.idade)

