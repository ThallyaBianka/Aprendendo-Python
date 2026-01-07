class Pessoa:
    def __init__(self, nome, idade = 20):
        self.nome = nome
        self.idade = idade
    def saudacao(self):
        print(f"Olá, lhe dou as boas-vindas {self.nome}")    

individuo = Pessoa("Thallya")

individuo.saudacao()