""" Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever
uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o
aluno é aprovado). Escrever também a média calculada. """

print("Média Aluno")

nome = input("Digite o nome do luno: ")
nota1 = int(input("Digite a nota do aluno na primeira prova: "))
nota2 = int(input("Digite a nota do aluno na segunda prova: "))

media = (nota1 + nota2) / 2

print(f"A média do aluno {nome} foi: {media}")

if media < 6:
    print("Reprovado")
else:
    print("Aprovado")