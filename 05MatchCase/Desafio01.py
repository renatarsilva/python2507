# DESAFIO 01
"""
Escreva um programa que solicite ao usuário uma nota inteira entre 0 e 10.
Use o comando `match case` para classificar a nota de acordo com a tabela a seguir:

- 0-4: Nota Baixa
- 5-7: Nota Média
- 8-9: Nota Alta
- 10: Nota Excelente

Exiba a classificação correspondente.
"""
nota = int(input("Digite sua nota: "))

match nota:
    case 1 | 2 | 3 | 4:
        print("\nNota Baixa")
    case 5 | 6 | 7:
        print("\nNota Média")
    case 8 | 9:
        print("\nNota Alta")
    case 10:
        print("\nNota Excelente")
    case _:
        print("\nNota Nota inválida...")
