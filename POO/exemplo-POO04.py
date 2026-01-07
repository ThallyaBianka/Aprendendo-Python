class Pessoa:
    def __init__(self, nome, idade = 20):
        self.nome = nome
        self.idade = idade

pessoa01 = Pessoa("Thallya")
pessoa02 = Pessoa("José", 18)
print(f"Nome: {pessoa01.nome}\nIdade: {pessoa01.idade}")
print(f"Nome: {pessoa02.nome}\nIdade: {pessoa02.idade}")