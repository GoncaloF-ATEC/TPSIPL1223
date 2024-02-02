"""

git basico




var
opt
    funcs (def)
cond (if, match)
loops (for e while)

tuplos
lista
dict
set
tuplos



dataclass
classes
herança


gestao de erros


"""

"""

() <- tuplos
[] <- lista (array)
{} <- set

{:} <- dict

{"nome": "Gonçalo", 
"idade": 18} 

"""
tp = ("Gonçalo", 12, "ATEC")

print(tp[0])
print(tp[1])
print(tp[2])

print("---")
for i in tp:
    print(i)

tp = tp + (4, )

print(tp)


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lista[0])
print(lista[3])


print(len(lista))
print(lista.__len__())

print(lista)

lista.append(232)

print(lista)

lista.insert(2, 999)

print(lista)

# remove um valor
lista.remove(999)

print(lista)

# remove o conteudo da ulima pos
x = lista.pop()
print(x)

print(lista)

# remove o conteudo do index, neste caso 8

lista.pop(8)

print(lista)



lista2 = [
    "Principal Skinner",
    "Homer Simpson",
    "Marge Simpson",
    "Bart Simpson",
    "Lisa Simpson",
    "Maggie Simpson",
    "Ned Flanders",
    "Mr. Burns",
    "Krusty the Clown",
    "Moe Szyslak",
    "Principal Skinner"
]

print(lista2)

x = lista2.pop(4)

print(x)
print(lista2)

lista2.remove("Principal Skinner")

print(lista2)


lista3 = [
    "Homer Simpson", "Marge Simpson", "Bart Simpson", "Lisa Simpson", "Maggie Simpson",
    "Ned Flanders", "Mr. Burns", "Krusty the Clown", "Moe Szyslak", "Principal Skinner",
    "Edna Krabappel", "Milhouse Van Houten", "Ralph Wiggum", "Chief Wiggum", "Apu Nahasapeemapetilon",
    "Barney Gumble", "Lenny Leonard", "Carl Carlson", "Sideshow Bob", "Mayor Quimby",
    "Dr. Hibbert", "Reverend Lovejoy", "Kent Brockman", "Groundskeeper Willie", "Patty Bouvier",
    "Selma Bouvier", "Kirk Van Houten", "Luann Van Houten", "Nelson Muntz", "Jimbo Jones",
    "Dolph Starbeam", "Kearney Zzyzwicz", "Fat Tony", "Hans Moleman", "Snake Jailbird",
    "Comic Book Guy", "Professor Frink", "Cletus Spuckler", "Gil Gunderson", "Mrs. Krabappel",
    "Bumblebee Man", "Helen Lovejoy", "Disco Stu", "Rod Flanders", "Todd Flanders",
    "Maude Flanders", "Sherri", "Terri", "Terri", "Terri"
]

print("---" * 10)

"""

lista[1 elm: ultimo elm: step] 



"""

print(lista3)
print(lista3[:5])
print(lista3[3:8])
print(lista3[2:20:3])

print(lista3[40:])

print(lista3[::-1])

print(lista3[:-5])
print(lista3[-5:])

lista3.sort()
print(lista3)

lista3.sort(reverse=True)
print(lista3)

print(lista3.count("Terri"))




print("-----------------Set---------------------")

myset = {3, 4, 1, 5, 2, 6}
print(myset)

myset.add(50)

print(myset)

myset.remove(3)

print(myset)
myset.add(50)

r1 = {"Polvilho Doce",
      "Polvilho Azedo",
      "Leite",
      "Oleo",
      "Ovos",
      "Sal",
      "Queijo"
      }

r2= {"Farinha",
      "Ovos",
      "Açucar",
      "Fermento",
      "Chocolate",
      "Manteiga",
      "Sal"
      }

print(r1.union(r2))
print(r1.intersection(r2))
print(r1.difference(r2))
print(r1.symmetric_difference(r2))

r1.intersection_update(r2)

r2.remove("Ovos")
print(r2)

elm = r2.pop()

print(elm)
print(r2)

print("-----------------dict---------------------------")

dict = {"key": "Value", "key2": "Value"}
print(dict)
print(dict["key"])


dict2 = {
    "Homer": "Pai da família",
    "Marge": "Mãe da família",
    "Bart": "Filho mais velho",
    "Lisa": "Filha do meio",
    "Maggie": "Bebe da família"
}

print(dict2["Homer"])

dict2["Moe"] = "Dono do bar"

print(dict2)


print("------")

del dict2["Moe"]

print(dict2)

print("------")

dict2["Moe"] = "Dono do bar"

dict2.pop("Moe")

print(dict2)

# dict2.popitem() <- utilidade discutivel
dict2.popitem()

print(dict2)


print(dict2.keys())

print(dict2.values())


print("------")
for i in dict2.keys():
    print(i)
print("------")
for i in dict2.values():
    print(i)

print("------")

for i in dict2.items():
    print(i)



print("---------------unpack---------------")

#tp = ("Gonçalo", 12, "ATEC")

tp = ["Gonçalo", 12, "ATEC"]
nome, idade, escola = tp

print(nome)
print(idade)
print(escola)

print("----")


par1, par2 = {"key": "Value", "key2": "Value"}.items()

print(par1)
print(par2)