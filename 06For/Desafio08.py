# DESAFIO 08
"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

maiores = float('-inf')
menores = float('inf')

for i in range(1, 8):
    ano = float(input(f"Digite o {i}°"))
    if ano > maiores:
        maior = ano
    if ano < menores:
        menor = ano



print(f"\n {maiores} Pessoas atingiram a maior idade")
print(f"{menores} Pessoas não atingiram a maior idade")
