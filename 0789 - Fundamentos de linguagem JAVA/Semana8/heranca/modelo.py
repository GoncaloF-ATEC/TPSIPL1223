class _Pessoa: # class pvt
    def __init__(self, nome: str, telefone: int):
        self.nome = nome
        self.telefone = telefone

    def mudar_telefone(self,
                       novo_telefone: int,
                       indicativo: int = None ):

        self.telefone = novo_telefone


    """
    
    publica - é visivel em todo o lado 
    
    nome
    """
    def get_info(self): # pub
        return f"nome: {self.nome}, telefone: {self.telefone}"

    """

    protected - é visivel na propria class e nas sub classes
    
    _nome
    """
    def _get_info2(self): # prot
        pass

    """

    privada - é visivel na propria class
    
    __nome
    """
    def __get_info3(self): # pvt
        pass

    def myDef(self):
        self.__get_info3()

class Formador(_Pessoa):
    pass

class adm(_Pessoa):
    pass

class gestor(_Pessoa):
    pass

class direcao(_Pessoa):
    pass


class Aluno(_Pessoa):

    def __init__(self, nome: str, telefone: int, turma: str):
        self.turma = turma
        super().__init__(nome, telefone)


    def myFunc(self):
        super()._get_info2()

    def get_info(self):
        return f"{super().get_info()}, turma: {self.turma}"





al = Aluno("Carlos", "123456", "TPSIPL1223")
print(al.nome)

al.get_info()
al.myFunc()


print(al.get_info())


