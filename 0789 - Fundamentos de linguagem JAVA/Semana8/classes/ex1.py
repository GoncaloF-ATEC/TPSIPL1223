"""
Classe Bola: Crie uma classe que modele uma bola: <- done

Atributos:
    Cor                 <- done
    circunferência      <- done
    material            <- done
Métodos:
    trocaCor            <- done
    mostraCor           <- done

"""

class Bola:
    def __init__(self, cor: str, circunferencia: float, material: str):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor: str):
        self.cor = nova_cor

    def mostraCor(self):
        print(f"a Cor da bola é: {self.cor}")