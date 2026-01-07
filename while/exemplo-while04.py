""" c) Elaborar um programa que apresente no final o somatório dos valores pares existentes na faixa de 1 até 500. """

contadora = 1
somatoria = 0

while contadora <= 500:
    if contadora % 2 == 0:
        somatoria = somatoria + contadora
    print(f"{somatoria} + {contadora} = {somatoria}")
    contadora += 1