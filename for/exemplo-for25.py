"""  j) Elaborar um programa que apresente os valores de conversão de graus Celsius em Fahrenheit, de 
10 em 10 graus, iniciando a contagem em 10 graus Celsius e finalizando em 100 graus Celsius. O 
programa deve apresentar os valores das duas temperaturas. A fórmula de conversão, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.  """

for contadora in range (0, 100, 10):
    soma = (contadora * 1.8) + 32
    print(f"O valor da conversão é: {soma}")