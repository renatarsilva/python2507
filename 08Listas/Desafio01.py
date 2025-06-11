# DESAFIO 01

"""
Faça um programa que leia 5 valores numéricos e
guarde-os em uma lista. No final, mostre qual foi
o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
lista = []
for num in range(1, 6):
    numero = int(input(f"Digite o {num}º número: "))
    lista.append(numero)


print(f"\nO maior nº é o {max(lista)} e está na {lista.index(max(lista))+1}ª posição.")
print(f"O menor nº é o {min(lista)} e está na {lista.index(min(lista))+1}ª posição.")