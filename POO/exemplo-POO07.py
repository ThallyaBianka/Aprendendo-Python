class Carro:
    def __init__(self, cor, marca, modelo):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo

    def mostrarInformações(self):
        print(f"Informações do carro\n\nModelo: {self.modelo}\nMarca: {self.marca}\nCor: {self.cor}")    

automovel = Carro("Vermelho", "Jeep", "Compass")

automovel.mostrarInformações()