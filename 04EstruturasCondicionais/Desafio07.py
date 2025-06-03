# DESAFIO 07
"""
Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de
10%.
Para salários inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input("Digite seu salário: "))
aumento10 = salario + (salario * (10/100))
aumento15 = salario + (salario * (15/100))

print(salario)

if salario <= 1250:
    print(f"Seu novo salário será {aumento15}")
else:
    print(f"Seu novo salário será:{aumento10}")     