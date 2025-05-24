# DESAFIO 05
"""
Crie um programa que dados o valor, a taxa e o tempo, efetuar o cálculo do valor de
uma prestação em atraso.
FÓRMULA: valor da prestação + (valor da prestação * (taxa / 100) * tempo)
"""
valor = int(input("Digite o valor da prestação: "))
taxa = float(input("Digite a taxa: "))
tempo = int(input("Digite os meses: "))

print(f'O valor a ser pago é: R${valor + (valor * (taxa / 100) * tempo):,.2f}')