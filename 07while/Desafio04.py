# DESAFIO 04
"""
Crie um programa que leia vários números inteiros pelo teclado. O
programa só vai parar quando o usuário digitar o valor 999, que é a
condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o 999).
"""
soma = 0
cont = 0

while True:
    n = int(input("Digite um número inteiro (999 para sair): "))
    if n == 999:
        print("\nFinalizando os cálculos...")
        break
    soma +=n
    cont += 1

    print(f"\nAsoma dos números: {soma}")
    print(f"\nQuantidade dos números: {cont}")