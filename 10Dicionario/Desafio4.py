# DESAFIO 04 BÔNUS
"""
Faça com que o programa anterior possa cadastrar uma quantidade de alunos escolhida pelo usuário.
No final apresente as informações tabuladas.
"""
from google.colab import output
alunos = []
aluno = {}


for i in range(int(input("Digite o número de alunos para cadastrar: "))):
    output.clear()
    aluno['nome'] = input(f"Digite o {i+1}º nome: ").upper()
    aluno['media'] = float(input(f"Digite a {i+1}ª média: "))
    media = aluno['media']
    match media:
        case _ if media < 5:
            aluno['situacao'] = 'REPROVADO'
        case _ if media < 7:
            aluno['situacao'] = 'EXAME'
        case _:
            aluno['situacao'] = 'APROVADO'
    alunos.append(aluno.copy())


output.clear()
print(f"\033[0;95m{'ALUNOS'.center(15)} {'MÉDIA'.center(5)} {'SITUAÇÃO'.center(11)}\033[0m")
for aluno in alunos:
    print(f"\033[0;30;47m {aluno['nome']:<15} {aluno['media']:^5} {aluno['situacao']:^11} ")
