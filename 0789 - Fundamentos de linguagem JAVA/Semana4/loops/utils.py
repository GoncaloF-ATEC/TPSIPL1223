def ola_mundo():
    print("Ola Mundo")


def ola_mundo2():
    print("Ola Mundo2")


def ola_mundo3(nome):
    print(f"Ola Mundo3 {nome}")


def ola_mundo4(nome: str): # nome: type hint
    print(f"Ola Mundo3 {nome}")


def ola_mundo5(nome: str, ano: int):
    msg = f"Ola Mundo3 {nome}, ano: {ano}"
    return msg
