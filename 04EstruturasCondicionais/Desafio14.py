# DESAFIO 14
"""
Faça um programa que leia três números e mostre qual é o
maior e qual é o menor.
"""
num1 = int(input("Digite o 1ª número: "))
num2 = int(input("Digite o 2ª número: "))
num3 = int(input("Digite o 3ª número: "))

# Verifica o maior número

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else: maior = num3

#verifica o menor numero

if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
else: menor = num3

print(f"Maior {maior}")
print(f"Menor {menor}")