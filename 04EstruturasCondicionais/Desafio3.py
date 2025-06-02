#desafio3

"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, exemplo:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
SOCORRAM ME SUBI NO ONIBUS EM MARROCOS
"""

frase = input("Digite um palavra: ")
espelho = frase [::-1].lower().replace(' ','')

if frase.lower().replace(' ','') == espelho:
    print(f"A {frase} é palíndromo")
else:
    print(f"A {frase} não é palíndromo")   