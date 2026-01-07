""" b) Apresentar os resultados de uma tabuada de multiplicar (de 1 até 10) de um número qualquer.  """

valor = int(input("Digite o valor a ser multiplicado: "))

for contadora in range(1, 11):
    i = valor * contadora
    print(f"{valor} x {contadora} é igual a = {i}")
