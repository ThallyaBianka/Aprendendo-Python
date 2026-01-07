""" As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem
compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e
escreva o custo total da compra. """

compraUsuario = int(input("Digite a quantidade de maçãs compradas: "))

if compraUsuario < 12:
    macas = 1.30
else:
    macas = 1.00
custoMaca = compraUsuario * macas
print(f"O valor da sua compra é: R${custoMaca:.2f}")