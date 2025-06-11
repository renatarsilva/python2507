# DESAFIO 02
"""
Faça um programa onde o computador vai “pensar” em um número entre 1 a 10.
O jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
"""

import random
tentativa = 0

pc = random.randint(1,10)

while True:
    pergunta = int(input("Digite um número: 1 a 10: "))
    if pergunta != pc:
        print("Você errou!!")
    else:
        print(f"Acertou com {tentativa} tentativas")
        break
    tentativa += 1
