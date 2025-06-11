# DESAFIO 03
"""
Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""

soma = 0;

while True:
    n1 = float(input("Digite valor 1: "))
    n2 = float(input("Digite valor 2: "))
    op = input("""
    Escolha uma opção:

    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa

    """)


    match op:
        case "1":
            print(f"{n1}+{n2} = {n1+n2}")
        case "2":
            print(f"{n1}X{n2} = {n1*n2}")
        case "3":
            print(f"\nO maior número é: {max(n1, n2)}")
        case "4":
            print("\nEscolha os novos números:")
            continue
        case "5":
            print("\nVocê saiu do programa!")
            break
        case _:
            print("Algo de errado não está certo")
