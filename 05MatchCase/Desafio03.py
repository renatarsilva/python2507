# DESAFIO 03
"""
Crie um programa que peça ao usuário para inserir um número de 1 a 7,
onde cada número representa um dia da semana (1 para domingo, 2 para segunda-feira
e assim por diante).
Use match case para imprimir o nome do dia da semana correspondente.
"""
dia = int(input("Digite o dia da semana (1 a 7): "))

match dia:
    case 1:
        print("\nDomingo")
    case 2:
        print("\nSegunda-feira")
    case 3:
        print("\nTerça-feira")
    case 4:
        print("\nQuarta-feira")
    case 5:
        print("\nQuinta-feira")
    case 6:
        print("\nSexta-feira")
    case 7:
        print("\nSábado")
    case _:
        print("\nDia inválido!")
