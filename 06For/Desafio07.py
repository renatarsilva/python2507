"""
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""
maior = float('-inf')
menor = float('inf')


for i in range(1, 6):
    peso = float(input(f"Digite o {i}º peso: "))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso


print(f"\nMaior peso: {maior} kg")
print(f"Menor peso: {menor} kg")