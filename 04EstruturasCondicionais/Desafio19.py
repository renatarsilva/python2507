# DESAFIO 19
"""
Faça um programa que leia um ano qualquer e mostre se ele é
BISSEXTO.
O ano bissexto ocorre a cada 4 anos (exceto em anos múltiplos
de 100 que não são múltiplos de 400)
"""

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 4 == 0):
    print("É ANO BISEXTO")
else:
    print("Não é ano bisexto")    