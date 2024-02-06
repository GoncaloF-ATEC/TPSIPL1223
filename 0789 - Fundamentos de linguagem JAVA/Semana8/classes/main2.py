import ex1

cor = input("digite a cor: ")
circ = input("digite a circunferência: ")
material = input("Qual o material: ")

bola = ex1.Bola(cor,circ,material)

print("---" * 10)
bola.mostraCor()

print("---" * 10)
nova_cor = input("digite a nova cor: ")
bola.trocaCor(nova_cor)
bola.mostraCor()
