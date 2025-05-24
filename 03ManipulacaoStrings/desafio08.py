# DESAFIO 03
"""
Faça um programa que leia uma frase pelo teclado e mostre:

Quantas vezes aparece a letra "A"
Em que posição ela aparece a primeira vez
Em que posição ela aparece a última vez
"""

frase = str(input("Digite sua frase: \n")).lower().replace(' ','')

print(f"Sua frase tem {frase.lower().count('a')} letras 'A'.")
print(f"O 'A' aparece pela 1° vez na posição: {frase.find('a')+1}")
print(f"O A aparece pela última vez na posição: {frase.rfind('a')+1}")