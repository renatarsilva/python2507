# DESAFIO 06
"""
Crie um programa que leia um número inteiro e mostre na tela
se ele é PAR ou IMPAR.
"""
import random

numero = random.randint(1,500)

print(numero)

print('par' if numero % 2 == 0 else 'impar')
