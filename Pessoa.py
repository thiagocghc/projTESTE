class Pessoa:
    def __init__(self,id,nome,idade):
        self.id = id
        self.nome = nome
        self.idade = idade

    def getNome(self):
        return self.nome
    
    def setIdade(self,novaIdade):
        self.idade = novaIdade


pessoa1 = Pessoa(1,"Wendril",18)

print(pessoa1.id)
print(pessoa1.getNome())
print(pessoa1.idade)
print("###"*8)
##### SETAR -> ALTERAR -> EDITAR
pessoa1.setIdade(23)
print(pessoa1.idade)


