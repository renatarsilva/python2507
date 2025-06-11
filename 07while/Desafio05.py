# DESAFIO 05
"""
Crie um programa que leia vários números inteiros pelo teclado. No
final da execução, mostre a média entre todos os valores e qual foi o
maior e o menor valores lidos. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores
*Novos métodos para maior e menor (max/min) exemplo:
print(max(20, 4, 89, 2))
print(min(20, 4, 89, 2))
"""

soma = 0
cont = 0
maior = float('-inf')
menor = float('inf')

while True:
    n = float(input("Digite um número inteiro: "))
    if n == 999:
        print("\nFinalizando os cálculos...")
        break
    soma +=n
    cont += 1
    maior = max(maior, n)
    menor = max(menor, n)

print(f"\nA média dos números: {soma/cont:,.1f}")
print(f"\nQuantidade dos números: {maior}")
print(f"\nQuantidade dos números: {menor}")
