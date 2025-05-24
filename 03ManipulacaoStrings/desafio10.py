# DESAFIO 05
"""
Refazer o DESAFIO 03 escolhendo a letra para contar e desconsiderar espaços.
-
Faça um programa que leia uma frase pelo teclado e mostre:

Quantas vezes aparece a letra "A"
Em que posição ela aparece a primeira vez
Em que posição ela aparece a última vez
"""

frase = str(input("Digite sua frase: \n")).upper().replace(''," ")
letra = str(input("Digite sua frase: \n")).upper()


print(f"\nSua frase tem {frase.count(letra)} letras {letra}.")
print(f"{letra} aparece pela 1° vez na {frase.find(letra)+1}° posição")
print(f"{letra} aparece pela última vez na {frase.rfind(letra)+1}° posição")