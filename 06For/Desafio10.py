# DESAFIO 10
"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
>1 só é divisível por ele mesmo
"""

cont = 0
n = int(input("Digite um número: "))
for i in range(1, n):
    if n%i == 0:
        cont+=1
    if cont > 1:
        break


if cont > 1:
    print("\nNão é primo 👎")
else:
    print("\nÉ primo 👍")