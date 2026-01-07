""" Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela
poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu) """

print("Idade para Votar")

anoDeNascimento = int(input("Digite o seu ano de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))
idade = anoAtual - anoDeNascimento

if idade < 16:
    print("Você não pode votar.")

elif idade < 18:
    print("Seu voto é opcional.")
else:
    print("Seu voto é obrigatório!")