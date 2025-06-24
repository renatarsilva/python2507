# DESAFIO 03 v1


alunos = {}


alunos['nome'] = input("Digite seu nome: ").upper()
alunos['media'] = float(input(f"Digite sua média: "))
media = alunos['media']


match media:
    case _ if media < 5:
        alunos['situacao'] = 'Reprovado'
    case _ if media < 7:
        alunos['situacao'] = 'Exame'
    case _:
        alunos['situacao'] = 'Aprovado'


print(alunos)