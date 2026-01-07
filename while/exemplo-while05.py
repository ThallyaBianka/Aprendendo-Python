""" d) Apresentar todos os valores numéricos inteiros ímpares situados na faixa de 0 a 20. Para verificar
se o número é ímpar, efetuar dentro da malha a verificação lógica desta condição com a instrução
se, perguntando se o número é ímpar; sendo, mostre-o; não sendo, passe para o próximo passo """

contadora = 1

while contadora <= 20:

    if contadora % 2 == 1:
        print(contadora)
    contadora += 1