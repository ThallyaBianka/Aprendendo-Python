class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
pessoa1 = Pessoa("Thallya", 20)

print(pessoa1.nome)
print(pessoa1.idade)