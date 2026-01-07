def funcaoSalada(a, b, /, *, c, d):
    return a + b + c + d

resultado = funcaoSalada(1, 2, c = 3, d = 4)
print(resultado)