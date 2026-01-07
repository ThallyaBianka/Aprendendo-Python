def funcaoCarro(carro):
    print("Nome:", carro["nome"])
    print("Chassi:", carro["chassi"])
    print("Marca:", carro["marca"])
    print("Modelo:", carro["modelo"])
    print("Ano de fabricacao:", carro["anoFabricacao"])
    print("Cor:", carro["cor"])
    print("Tipo de combustivel:", carro["tipoCombustivel"])
    print("Placa do carro:", carro["placaCarro"])

classeCarro = {
    "nome": "Judite 17 + 1",
    "chassi": "abcd0123456789e",
    "marca": "Chevrolet",
    "modelo": "Opala",
    "anoFabricacao": 1990,
    "cor": "Azul",
    "tipoCombustivel": "Gasolina",
    "placaCarro": "ABC1234",
}
funcaoCarro(classeCarro)
