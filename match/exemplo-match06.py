idade = int(input("Digite sua idade: "))
 
match idade:
    case idade if idade < 12:
        print("Crianca")
    case idade if idade >= 12 and idade <= 17:
        print("Adolescente")
    case idade if idade >= 18 and idade < 59:
        print("Adulto")
    case idade if idade >= 60:
        print("Idoso")
    case _:
         print("Operação inválida!")
 