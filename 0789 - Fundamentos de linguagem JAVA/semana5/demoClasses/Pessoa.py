from dataclasses import dataclass

@dataclass
class Pessoa:
    # Atributos
    nome: str
    idade: int
    genero: str

    # métodos

    def envelhecer(self, anos: int = 1):
        self.idade += anos # self.idade = self.idade + anos
        # i++ <- i += 1