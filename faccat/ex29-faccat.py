""" Soma dos dois maiores valores """

valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))
valor3 = int(input("Digite o terceiro número: "))

if valor1 < valor2 and valor2 <= valor3:
    soma = valor2 + valor3
    print(f"Os maiores números é o segundo e terceiro: {valor2} + {valor3} = {soma}")
elif valor3 < valor1 and valor1 <= valor2:
    soma = valor1 + valor2
    print(f"Os maiores números é o primeiro e segundo: {valor1} + {valor2} = {soma}")
else:
    soma = valor1 + valor3
    print(f"Os maiores números é o primeiro e terceiro: {valor3} + {valor1} = {soma}")