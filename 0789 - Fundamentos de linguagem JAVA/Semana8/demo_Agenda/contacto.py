from dataclasses import dataclass


@dataclass()
class Morada:
    localidade: str
    teste: str
    def __init__(self, localidade: str):
        self.localidade = localidade
        self.teste = "txt"



class Contacto:
    __nome: str
    __telefone: int
    __email: str
    __moradas: Morada

    def __init__(self,
                 nome: str,
                 telefone: int,
                 email: str = None,
                 morada: Morada = None):

        self.__nome = nome.capitalize()
        self.__telefone = telefone
        self.__email = email
        self.__morada = morada

    def get_info(self):
        return (self.__nome, self.__telefone, self.__email, self.__morada)

    def edit_info(self,
                  nome: str = None,
                  telefone: int = None,
                  email: str = None,
                  morada: Morada = None):

        if nome is not None:
            self.__nome = nome

        if telefone is not None:
            self.__telefone = telefone

        if email is not None:
            self.__email = email

        if morada is not None:
            self.__morada = morada