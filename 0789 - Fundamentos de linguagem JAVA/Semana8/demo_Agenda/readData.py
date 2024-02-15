
print("inicio")


file = open("ErrorLog.txt", "r")

# print(file.read()) #<- le tudo
#  print(file.read(n))  #<- le n chars
# print(file.readline()) #<- le uma linha

"""
linhas = file.readlines()

for l in linhas:
    print(l)

print("fim")
"""

"""
print(file.readlines())
[
    '2024-02-09 21:38:16.818520\tDataError\to contacto e o nome nao podem ser adicionados ao mesmo tempo\n', 
    '2024-02-09 21:42:34.766656\tDataError\to contacto e o nome nao podem ser adicionados ao mesmo tempo\n',
    '2024-02-09 21:43:16.046948\tdivZero o contacto e o nome nao podem ser adicionados ao mesmo tempo'
 ]


print(file.read())
2024-02-09 21:38:16.818520	DataErr e o nome nao podem ser adicionados ao mesmo tempo
2024-02-09 21:43:16.046948	divZero o contacto e oor	o contacto e o nome nao podem ser adicionados ao mesmo tempo
2024-02-09 21:42:34.766656	DataError	o contacto nome nao podem ser adicionados ao mesmo tempo


"""

"""
linha1 = file.readline()
linha1 = linha1.split("\t")
print(linha1)
linha1[-1] = linha1[-1].replace("\n", "")
print(linha1)
"""

class erro:

    def __init__(self, erro):
        erro_local = erro.split("\t")

        self.data = erro_local[0]
        self.erro = erro_local[1]
        self.msg = erro_local[-1].replace("\n", "")

    def  __str__(self):
        return f"erro: {self.erro}\ndata: {self.data}\nmsg: {self.msg}"


file = open("ErrorLog.txt", "r")

for linha in file.readlines():
    myerro = erro(linha)
    print(myerro)
    print("----" * 10)


file = open("ErrorLog.txt", "r")

linha1 = file.readlines()
print(linha1)

"""
linha1 = linha1.split("\t")
print(linha1)
linha1[-1] = linha1[-1].replace("\n", "")
print(linha1)
"""