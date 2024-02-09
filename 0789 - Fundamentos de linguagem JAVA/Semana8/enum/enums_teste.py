from enum import Enum



class Estacoes_ano(Enum):
    Primavera = "Primavera"
    Verao = "-> Verão <-"
    Outono = "Outono"
    Inverno = "Inverno"

print(type(Estacoes_ano.Verao))
print(type(Estacoes_ano.Verao.name))
print(type(Estacoes_ano.Verao.value))

for i in Estacoes_ano:
    print(i.name)

print(
    Estacoes_ano("-> Verão <-") # recebe um valor que tem de estar numa das opts
)

