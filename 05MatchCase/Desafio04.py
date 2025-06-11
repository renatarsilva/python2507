# DESAFIO 04
"""
Implemente uma calculadora simples que realiza as operações de adição, subtração, multiplicação e divisão.
O usuário deve inserir dois números e, em seguida, selecionar a operação desejada (+, -, *, /).
Use o comando match case para realizar a operação correta e exibir o resultado.
"""
num1 = float(input("Digite o 1º número: "))
oper = input("""Escolha a operação:
[+] Somar
[-] Subtrair
[*] Multiplicar
[/] Dividir
""")
num2 = float(input("Digite o 2º número: "))
match oper:
    case '+':
        print(f"\n{num1} + {num2} = {num1+num2}")
    case '-':
        print(f"\n{num1} - {num2} = {num1-num2}")
    case '*':
        print(f"\n{num1} x {num2} = {num1*num2}")
    case '/':
        if num2 != 0:
            print(f"\n{num1} / {num2} = {num1/num2}")
        else:
            print("\nNão pode ser divisível por 0! Jumento! 🐴")
    case _:
        print("\nOpção inválida...")

