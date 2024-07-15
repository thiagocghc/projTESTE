####SUPER CLASS
class Filme:
    def __init__(self,nome,duracao):
        self._nome = nome        ###ATRIBUTO PROTEGIDO -> 1 _ underline -> as subclass podem acessar esse atributo
        self.__duracao = duracao ###ATRIBUTO PRIVADO 2 __ underline

    def setNome(self,novo_nome):
        self._nome = novo_nome

    def getNome(self):
        return self._nome

    def play(self):
        print(f" {self._nome} começou...")

    def getDuracao(self):
        return self.__duracao
        
#####SUBCLASS
class Drama(Filme):
    def __init__(self, nome, duracao,ator):
        super().__init__(nome, duracao)
        self.ator = ator
    
    def play(self):
        print(f" {self._nome} começou a chorar...")

class Acao(Filme):
    def __init__(self, nome, duracao,expolosivos):
        super().__init__(nome, duracao)
        self.expolosivos = expolosivos
    
    def play(self):
        print(f" {self._nome} começou a explodir...")
