# DESAFIO 02
"""
Faça um programa que leia um número de quatro dígitos entre 1000 a 9999 e mostre na tela
cada um dos dígitos separados.
Ex: Digite um numero: 1981

Unidade: 1
Dezena: 8
Centena: 9
Milhar: 1
"""

num = str(input("quatro dígitos entre 1000 a 9999 \n "))
uni = num [3]
dez = num [2]
cen = num [1]
mil = num [0]

print(f'Unidade:{uni}')
print(f'Dezena:{dez}')
print(f'Centena:{cen}')
print(f'Milhar:{mil}')
