# DESAFIO 10
"""
Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com sua idade:


Se ele ainda vai se alistar ao serviço militar
Se é a hora de se alistar
Se já passou o tempo do alistamento


Seu programa também deverá mostrar o tempo que falta ou
que passou do prazo.
"""

import datetime

nascimento = int(input("Digite o ano do nascimento: "))
anoAtual = datetime.date.today().year
dif = anoAtual - nascimento

if dif <=17:
    print("Ainda vai se alistar ao serviço militar")
elif dif == 18:
    print("é a hora de se alistar")
else:
    print("Já passou o tempo do alistamento")