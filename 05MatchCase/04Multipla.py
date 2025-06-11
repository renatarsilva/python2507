
numero = int(input("Digite um número: "))
multimo_numero = str(numero)[-1]


match ultimo_numero:
    case '1' | '3' | '5' | '7' | '9':
        print(f"\nO número {numero} é \033[31mÍMPAR\033[0m. ☝")
    case _:
        print(f"\nO número {numero} é \033[32mPAR\033[0m. ✌")