# DESAFIO 06
"""
Crie um programa que leia um número inteiro e mostre na tela
se ele é PAR ou IMPAR.
"""

import random

num = random.randint(1,50)

print(num)

if num % 2 == 0:
    print("Número é par")
else:
    print("Número é impar")    
