class Automovel:
    def __init__(self,marca,modelo,cor="Branco",ano=None,placa="ABC-1234"):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.placa = placa

    def ligar(self):
        print(f" {self.marca} Ligada!!!!!")

    def getDados(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Ano: {self.ano}")
        print(f"Placa: {self.placa}")


carro1 = Automovel("BMW","328i","Azul","1999","HSF-6666")
carro1.getDados()
carro1.ligar()



        