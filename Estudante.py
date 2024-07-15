class Estudante: #### DEFINIÇAO DA CLASSE
    def __init__(self,matricula,nome,idade,nota): ###MÉTODO CONSTRUTOR
        self.matricula = matricula #ATRIBUTO
        self.nome = nome #ATRIBUTO
        self.idade = idade #ATRIBUTO
        self.nota = nota  #ATRIBUTO

    def hello(self): #MÉTODO
        print(f" Olá {self.nome}")

    def mostrarDados(self): #MÉTODO
        print(f" Matricula: {self.matricula}")
        print(f" Nome: {self.nome}")
        print(f" Idade: {self.idade}")
        print(f" Nota: {self.nota}")
