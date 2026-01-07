mes = 5
dia = 4

match dia:
    case 1 | 2 | 3 | 4 | 5 if mes == 4:
        print("Uma semana em Abril")
    case 1 | 2 | 3 | 4 | 5 if mes == 5:
        print("Uma semana em Maio")
    case _:
        print("Número inválido!")