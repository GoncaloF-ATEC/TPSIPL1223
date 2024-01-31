a = 1
b = 4

print(f"a: {a}\nb: {b}")
b, a = a, b

print(f"a: {a}\nb: {b}")


print("-----------match-------------")

nota = ((3+5*4-1)**2)

match nota:
    case 10:
        print("aprovado")
    case 15:
        print("aprovado com mais nota")


nota = 10

print(nota >= 10 and nota <= 20)
print(10 <= nota <= 20)
print(10 <= nota and nota <= 20)
print(range(10, 21).__contains__(nota))
print(10 in range(10, 21))

