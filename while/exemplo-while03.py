""" a) Apresentar os resultados de uma tabuada de multiplicar (de 1 até 10) de um número qualquer. """

contadora = 1
numero1 = int(input("Digite um número: "))

while contadora <= 10:
    numero2 = numero1 * contadora
    print(f"{numero1} * {contadora} = {numero2}")
    contadora += 1