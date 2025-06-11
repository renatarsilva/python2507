# DESAFIO 08
"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
import random

maior_de_idade = 0
menor_de_idade = 0

numeroRand = random.randint(1950,)
idade = 2025 - numeroRand

for i in range(idade):
    if ano < 18:
        menor_de_idade += 1
    else:
        maior_de_idade +=1

print(f"{maior_de_idade} pessoa(as) são maior de idade")
print(f"{menor_de_idade} pessoa(as) são menor de idade")