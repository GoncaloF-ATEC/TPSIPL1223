from contacto import Contacto, Morada
from utils import DataError, divZero

class Agenda:
    def __init__(self):
        self.lista_contactos = []

    def add_contacto(self,
                    contacto: Contacto = None,
                    nome: str = None,
                    telefone: int = None):

        if contacto is not None and (nome is not None or telefone is not None):
            raise DataError("o contacto e o nome nao podem ser adicionados ao mesmo tempo")
            #raise DataError()

        if contacto is not None:
            self.lista_contactos.append(contacto)
        else:
            self.lista_contactos.append(Contacto(nome, telefone))



a = Agenda()

a.add_contacto(contacto=Contacto("<NAME>", 1234), nome= "<NAME>", telefone=1234)

c = Contacto("Armando", 1234, email="teste", morada=Morada("rua x"))
a.add_contacto(contacto=c)


n = "Pedro"
tlm = 3124123
a.add_contacto(nome=n, telefone=tlm)


