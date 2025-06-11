# DESAFIO 08 v2
"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

maior_de_idade = 0
menor_de_idade = 0

for i in range(1,8):
    idade = 2025-int(input(f"Digite o {i}° ano de nascimento"))
    if ano < 18:
        menor_de_idade += 1
    else:
        maior_de_idade +=1

print(f"{maior_de_idade} pessoa(as) são maior de idade")
print(f"{menor_de_idade} pessoa(as) são menor de idade")
