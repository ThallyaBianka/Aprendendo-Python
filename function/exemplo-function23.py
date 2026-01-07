def funcaoRecursividade(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(funcaoRecursividade(1, 2, 3))
print(funcaoRecursividade(10, 20, 30, 40))
print(funcaoRecursividade(5))
