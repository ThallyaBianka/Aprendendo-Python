class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def saudacao(self):
        return f"Olá {self.nome}! "

    def mensagem(self):
        mensagem = self.saudacao()
        print(f"{mensagem}Lhe dou as boas-vindas!")   

individuo = Pessoa("Gabriella")

individuo.mensagem()