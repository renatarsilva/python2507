# DESAFIO 13
"""
Escreva um programa que leia dois números inteiros e
compare- os, mostrando na tela uma mensagem:

O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais
"""

valor1 = int(input("Digite o 1 valor: "))
valor2 = int(input("Digite o 2 valor: "))

if valor1 > valor2:
    print(f"O primeiro valor é maior")
elif valor2 > valor1:
    print(f"O segundo valor é maior")
else:
    print(f"Não existe valor maior, os dois são iguais")       