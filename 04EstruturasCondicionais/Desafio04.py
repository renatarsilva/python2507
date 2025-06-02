# DESAFIO 04
"""
Escreva um programa que faça o computador sortear um
número inteiro entre 1 e 3 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou
perdeu.

Biblioteca necessária:
import random
random.randint(0, 1000)
"""

import random

numeroAleatorio = random.randint(1,10)

numeroJogador = int(input("Digite um número"))

if numeroJogador == numeroAleatorio:
    print("Você ganhou")
else:
    print("Você perdeu!")    


