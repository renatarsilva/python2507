# DESAFIO 04
"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.

Exemplo: Leandro Gomes Andrade

Primeiro: Leandro
Último: Andrade
"""

nomeCompleto = str(input("Digite seu nome completo"))
print(f'Primeiro:{nomeCompleto.title().split()[0]}')
print(f'Último:{nomeCompleto.title().split()[-1]}')