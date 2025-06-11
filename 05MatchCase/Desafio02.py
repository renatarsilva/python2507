# DESAFIO 02
"""
Refaça o DESAFIO 01 considerando notas com casas decimais.
"""
nota = float(input("Digite sua nota: "))

match nota:
    case _ if nota < 0:
        print("\nNota inválida...")
    case _ if nota < 5:
        print("\nNota Baixa")
    case _ if nota < 7:
        print("\nNota Média")
    case  _ if nota < 10:
        print("\nNota Alta")
    case 10:
        print("\nNota Excelente")
    case _:
        print("\nNota Nota inválida...")