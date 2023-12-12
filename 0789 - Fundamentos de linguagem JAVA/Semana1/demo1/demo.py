# Comentario numa linha

"""

Comsntario com
mais de
uma
linha

"""

"""

Int - num inteiro
flaot/double - num real 
str - txt
    char - letra
bool - V ou F

"""
# inferencia de tipos

idade = 10 # Var com numero  inteiro
nome = "Rui" # var ccom txt (String)
media = 10.6 # Var com numero real
aprovado = True # var com valor V ou F

#alterar conteudo de var
idade = 12
nome = "Joana"
media = 7.9
aprovado = False

# py deixa mas nao deve ser feito
idade = "Dez"

# "Sem" inferencia de tipos
nova_idade: int = 10 # nova_idade DEVE ser um int
novo_nome: str = 50 # nova_idade DEVE ser uma str mas recebe um int


# fazer o print de var
print(nova_idade)
print(novo_nome)
print(media)
print(idade)

# cirar str com var no meio

"""
nome = "Rui" # var ccom txt (String)
media = 10.6 # Var com numero real
aprovado = True # var com valor V ou F

O Rui tem media de 10.6"
"""

print("A", nome, "tem media de", media)
print(f"A {nome} tem media de {media}")