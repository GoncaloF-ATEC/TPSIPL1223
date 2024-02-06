
from dataclasses import dataclass

@dataclass
class Fruta:
    nome: str
    cor: str
    tamanho: float
    formato: str = None
    textura: str = None
    idade: int = 1
    comestivel: bool = True

    def envelhecer(self, anos: int = 1):
        self.idade += anos

        if self.idade > 5:
            self.comestivel = False


class Gato:
    nome: str
    def __init__(self, nome: str, idade: int = 0): # cira a class
        self.nome = nome
        self.idade = idade

    def envelhecer(self, anos: int = 1):
        self.idade = anos