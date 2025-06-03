# DESAFIO 15
"""
Escreva um programa que leia um número inteiro e peça para o
usuário escolher qual será a base de conversão:


1 para binário bin()
2 para octal oct()
3 para hexadecimal hex()
"""

numInt = int(input("Digite um numero inteiro: "))
conversao = input("""
Escolha a conversão:
[1] Binário
[2] Octal
[3] Hexadecimal
""")

if conversao == '1':    
    print(f"{numInt} em Binário: {bin(numInt)}")
elif conversao == '2':
    print(f"{numInt} em Octal: {oct(numInt)}")
elif conversao == '3':
    print(f"{numInt} em Hexadecimal: {hex (numInt)}")
else: 
    print("Conversão inválida!")          