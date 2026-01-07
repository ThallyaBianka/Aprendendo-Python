# Calcular o preço de um produto depois de um desconto aplicado

precoOriginal = float(input('Digite o preço original do produto: '))
percentualDesconto = int(input('Digite o percentual de desconto: '))
valorDesconto = precoOriginal * (percentualDesconto / 100)
precoFinal = precoOriginal - valorDesconto
print("O valor final do produto é: ", precoFinal)