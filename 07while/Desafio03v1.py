# DESAFIO 03 v2

from google.colab import output

while True:
    print("\n\033[41m", " CALCULADORA SENAI ".center(50), "\033[0m")
    n1 = float(input("\nDigite o 1º número: "))
    n2 = float(input("Digite o 2º número: "))
    op = input("""

ESCOLHA UMA OPÇÃO:

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do programa

""")
    match op:
        case '1':
            output.clear()
            print(f"Soma: {n1} + {n2} = {n1+n2}")
        case '2':
            output.clear()
            print(f"Multiplicação: {n1} x {n2} = {n1*n2}")
        case '3':
            output.clear()
            print(f"Maior número: {max(n1, n2)}")
        case '4':
            output.clear()
            print("Escolha os novos números: ")
            continue
        case '5':
            output.clear()
            print("Saindo...")
            break
        case _:
            output.clear()
            print("Algo de errado não está certo! 🤡")
