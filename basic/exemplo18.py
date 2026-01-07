# calcular o valor de aumento e o novo salário

salarioAtual = float(input('Digite o seu salário atual: '))
percentualAumento = int(input('Digite o percentual de aumento: '))
aumentoSalario = salarioAtual * (percentualAumento / 100)
precoFinal = salarioAtual + aumentoSalario

print("O valor do aumento é: ", aumentoSalario)
print("O valor final do produto é: ", precoFinal)