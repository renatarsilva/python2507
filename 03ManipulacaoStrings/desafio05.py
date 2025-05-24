# DESAFIO 01
"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
    O nome com todas as letras maiúsculas
    O nome com todas as letras minúsculas
    Quantas letras tem o primeiro nome
    Quantas letras ao todo (sem considerar espaços)
"""

nome = str(input("Digite seu nome:"))

print(nome.upper())
print(nome.lower())
print(nome.title())
print(nome.title().split()[0])

nome1 = nome.replace(' ', '')
nome2 = nome.title().split()[0]
print(len(nome2))
print(len(nome1))