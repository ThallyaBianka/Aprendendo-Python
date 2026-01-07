''' Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade
dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias. '''

print("Idade em Dias")

idade = int(input('Digite sua idade: '))
mes = int(input('Digite quantos meses se passou desde o seu último aniversário: '))
dias = int(input('Digite quantos dias se passou desde o seu último mesversário: '))

idade = idade * 365
mes = mes * 30
dias = dias + mes + idade

print("Sua idade em dias é:", dias)