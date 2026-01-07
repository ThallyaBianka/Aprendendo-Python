mes = int(input("Digite o número do mês entre Abril e Maio:"))
dia = int(input("Digite o número do dia da semana:"))

match dia:
    case 1 | 2 | 3 | 4 | 5 if mes == 4:
        print("Uma semana em Abril")
    case 1 | 2 | 3 | 4 | 5 if mes == 5:
        print("Uma semana em Maio")
    case _:
        print("Número inválido!")