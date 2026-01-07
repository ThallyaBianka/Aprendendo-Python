""" Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos
brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total
de eleitores """

votos = int(input("Digite o total de votos dos eleitores do município: "))
brancos = int(input("Digite o total de votos Brancos: "))
nulos = int(input("Digite o total de votos Nulos: "))
validos = int(input("Digite o total de votos Válidos: "))

percentualBrancos = (votos * brancos) / 100
percentualNulos = (votos * nulos) / 100
percentualValidos = (votos * validos) / 100

print("Votos brancos:", percentualBrancos, '%', "Votos Nulos:", percentualNulos, '%', "Votos Válidos:", percentualValidos, '%')