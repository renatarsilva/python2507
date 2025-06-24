# DESAFIO 02
"""
Crie um programa que gere cinco números aleatórios para uma tupla.
Exiba a listagem de números gerados, indique o menor e o maior valor.
"""

import random

numeros_aleatorios = []
for i in range(5):
    numeros_aleatorios.append(random.randint(1, 50))

tupla = tuple(numeros_aleatorios)
print(f"Tupla: {tupla}")
print(f"Maior valor: {max(tupla)}")
print(f"Menor valor: {min(tupla)}")