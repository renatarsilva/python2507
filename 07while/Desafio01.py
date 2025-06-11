# DESAFIO 01
"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os
valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até
ter um valor correto.

"""

from google.colab import output


while True:
    sexo = input("Digite (F) para Feminino (M) para masculino\n").upper()
    if sexo != 'M' and sexo != 'F':
        print("\nPor gentileza digite seu sexo (F/M)")
        continue
    if sexo == 'M':
        print("Sexo Masculino")
    else:
        print("Sexo Feminino")
    break