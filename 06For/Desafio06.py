# DESAFIO 06
"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
termo = int(input("Digite o termo: "))
razao = int(input("Digite a razão: "))
print("\nOs números da sua PA são: ", end=' ')
for i in range(9):
    if i == 0:
        print(termo, end=' ')
    termo += razao
    print(termo, end=' ')