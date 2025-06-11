# DESAFIO 04
"""
Faça um programa que mostre na tela uma contagem regressiva para
o estouro de fogos de artifício, indo de 10 até 0, com uma pausa
de 1 segundo entre eles.
Utilizar a Biblioteca time | time.sleep(segundos)
"""
from google.colab import output
import time
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
    output.clear()
print(" 🎆 FELIZ ANO NOVO!!! 🍾 ".center(50, '#'))