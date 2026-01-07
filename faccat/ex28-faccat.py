""" Qual o maior valor? """

valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))
valor3 = int(input("Digite o terceiro número: "))

if valor1 < valor2 and valor2 < valor3:
    print(f"O maior número é o terceiro número: {valor3}")
elif valor3 < valor1 and valor1 < valor2:
    print(f"O maior número é o segundo número: {valor2}")
else:
    print(f"O maior número é o primeiro número: {valor1}")
