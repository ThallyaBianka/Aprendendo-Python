class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def mostrarNome(self):
        print(f"Nome: {self.nome}")    

individuo = Pessoa("Thallya")

individuo.mostrarNome()