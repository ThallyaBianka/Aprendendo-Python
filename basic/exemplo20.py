# Verificar se é quadrado ou retângulo

print("Quadrado ou Retângulo?")
print()

altura = float(input("Digite o valor da altura: "))
base = float(input("Digite o valor da base: "))

print(f"Os valores digitados foram {base:.2f} e {altura:.2f}")
if altura == base:
    print("É um quadrado!")
else:
    print("É um retângulo!")