# DESAFIO 17
"""
A confederação Nacional de Natação precisa de uma programa
que leia o ano de nascimento de uma atleta e mostre sua
categoria, de acordo com a idade.


Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 24 anos: SÊNIOR
Acima: MASTER
"""

import datetime

nascimento = int(input("Digite o ano de nascimento"))
anoAtual = datetime.date.today().year
dif = anoAtual - nascimento

if dif <= 9:
    print("Mirim")
elif dif <= 14:
    print("Infantil")
elif dif <=19:
    print("Júnior")
elif dif <= 24:
    print("sênior")
else:
    print("Master")                
