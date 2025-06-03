# DESAFIO 12
"""
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
Condições Necessárias:
a + b > c
a + c > b
b + c > a
"""
a = int(input("Digite o comprimento da 1ª reta: "))
b = int(input("Digite o comprimento da 2ª reta: "))
c = int(input("Digite o comprimento da 3ª reta: "))

if a+b>c and a+c>b and b+c>a:
    print("\n\033[32mPode formar um triângulo")
else:
    print("\n\033[31mNão pode formar um triângulo")
