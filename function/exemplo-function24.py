def funcaoMaiorNumero(*numeros):
    if len(numeros) == 0:
        return None
    maiorNumero = numeros[0]
    for numero in numeros:
       if numero > maiorNumero:
           maiorNumero = numero
    return maiorNumero

print(funcaoMaiorNumero(3, 7, 2, 9, 1))
