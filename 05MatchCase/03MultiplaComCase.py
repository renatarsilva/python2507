# OPÇÃO MÚLTIPLA COM CASE _ IF

numero = int(input("Digite um número: "))

match numero:
    case 1 | 3 | 5 | 7 | 9:
        print("É ímpar entre 0 e 10")
    case _ if numero < 0:
        print("É negativo")
    case _:
        print("Um número qualquer...")