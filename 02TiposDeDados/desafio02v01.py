# DESAFIO 02 v1
"""
Escreva um programa que leia dois caracteres e imprima-os na tela da seguinte forma:
O usuário digitou (caractere1) e (caractere2)!.
"""

caractere1 = input("Digite um caractere:")
caractere2 = input("Digite outro caractere:")
print(f'O usuário digitou \033[1;31m {caractere1}\033[0m'
    f'e\033[1;31m{caractere2}\033[0m!')