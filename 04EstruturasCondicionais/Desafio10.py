# DESAFIO 09
"""
Escreva um programa para aprovar um empréstimo bancário
para a compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai
pagar.

Calcule o valor da prestação mensal, sabendo que ela não
pode exceder 30% do salário ou então o empréstimo será
negado.
"""

valorCasa = float(input("Digite o valor do imóvel: "))
salarioComprador = float(input("Digite o salário do comprador: "))
tempo = int(input("Digite anos de Financiamento: ")) * 12
trintaPorcento = salarioComprador*(30/100)
prestacao = valorCasa

if prestacao > trintaPorcento:
    print(f"\n\033[031mEmpréstimo negado. Parcela máxima:{trintaPorcento:,.2f}\033[0m")
else:
    print(f"\n\033[32mEmpréstimo aprovado. Parcela{prestacao:,.2f}\033[0m")

