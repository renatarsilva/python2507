# DESAFIO 06
"""
Dado a nota das provas P1, P2 e P3, calcular a média (aritmética)
das notas do aluno.
"""
aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota1: "))
nota2 = float(input("Digite a nota2: "))
nota3 = float(input("Digite a nota3: "))
media = (nota1+nota2+nota3)/3

if media >= 8:
    print(f'A média do {aluno} é {media}, e ele está\033[32m aprovado\033[')
elif media >=6:
    print(f'A média do {aluno} é {media}, e ele está em\033[033m recuperação')
else:
    print(f'A média do {aluno} é {media}, e ele está\033[031m reprovado')
