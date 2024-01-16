from datetime import datetime


def set_int(num:int) -> int:
    if type(num) is int:
        return num

    raise Exception(f"{num} não e um int")

try:
    num = set_int("fsdfds") # num  = 1
    print(num)
except:
    print("Erro ao executar")

print("passou")


minf  = datetime.now().time().minute + 1

c = 0
while True:
  #  print(datetime.now().time().second)
    if datetime.now().time().second == 59:
        c += 1

    if datetime.now().time().minute >= minf:
        break

print(c)
"""

interp:

py
php
js

sem print -> 991 373

236 173
242 322 - i9 32 py
283 685 ter
242 261 vs


298 690  - M1 16


201 674  - i5 32 

190 053  - i5 8gb

262 039  - i5

22 354  


code.py 

intwep 

maquina 



porg

maquina


"""