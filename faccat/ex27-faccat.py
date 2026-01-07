""" Positivo, Negativo ou Neutro """

valor = int(input("Digite um número: "))

if valor < 0:
    print("Negativo")
elif valor == 0:
     print("Neutro")
else:
    print("Positivo")