# DESAFIO 11
"""
Crie um programa que leia duas notas entre 0 a 10 de um aluno
e calcule sua média, mostrando uma mensagem no final, de
acordo com a média atingida.


Média abaixo de 5.0: REPROVADO
Média entre 5.0 a 6.9: RECUPERAÇÃO
Média igual ou superior a 7.0: APROVADO
"""

nota1 = float(input("Digite nota 1: "))
nota2 = float(input("Digite nota 2: "))
media = (nota1 + nota2) / 2

if nota1 < 0 or nota2 < 0 or nota1 > 10 or nota2 >10:
    print("Dgite uma nota válida")
elif media <5:
    print(f"Sua média é {media}, e você está reprovado")
elif media < 6.9:
    print(f"Sua média é {media}, e você está em recuperação")
else: 
    print(f"Sua média é {media}, e você está aprovado")        
