#Desafio 05

"""
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que
ele foi multado.

A multa custará R$ 7,00 por cada km acima do limite.
"""

import random

velocidade = random.randint(20, 210)
multa = (velocidade - 80) *7

if velocidade >= 80:
    print(f"Você ultrapassou o limite de velocidade, sua multa é de R${multa},00")
else:
    print("Velocidade permitida")    
