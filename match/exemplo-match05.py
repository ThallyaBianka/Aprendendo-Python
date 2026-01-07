numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operador = input("Digite um operador: ")

match operador:
    case "+":
         resultado = numero1 + numero2
         print(f"O resultado da operação é: {resultado}")
    case "-":
         resultado = numero1 - numero2
         print(f"O resultado da operação é: {resultado}")
    case "*":
         resultado = numero1 * numero2
         print(f"O resultado da operação é: {resultado}")
    case "/" if numero1 == 0:
         print("Não é possível realizar o cálculo")
    case "/":
         resultado = numero1 / numero2
         print(f"O resultado da operação é: {resultado}")
    case _:
         print("Operação inválida!")