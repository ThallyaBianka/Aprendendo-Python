class Carro:
    def __init__(
        self,
        modelo,
        tipoCombustivel,
        cor,
        placa,
        chassi,
        ano,
        cambio,
        freio,
        quilometragem,
        fabricanteCarro,
    ):
        self.modelo = modelo
        self.tipoCombustivel = tipoCombustivel
        self.cor = cor
        self.placa = placa
        self.chassi = chassi
        self.ano = ano
        self.cambio = cambio
        self.freio = freio
        self.quilometragem = quilometragem
        self.fabricanteCarro = fabricanteCarro


carro1 = Carro(
    "Sienna", "Flex", "Preto", "ABC1B34", "abcd123456789e", 2007, "Manual", "ABS", 44500, "Fiat"
)

print("Ficha do carro")
print("")
print("Modelo:", carro1.modelo)
print("Tipo de combustível:", carro1.tipoCombustivel)
print("Cor:", carro1.cor)
print("Placa:", carro1.placa)
print("Chassi:", carro1.chassi)
print("Ano:", carro1.ano)
print("Tipo de câmbio:", carro1.cambio)
print("Tipo de freio:", carro1.freio)
print("Quilometragem:", carro1.quilometragem)
print("Fabricante:", carro1.fabricanteCarro)