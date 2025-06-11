# OPÇÃO ÚNICA

operacao = input("""
ESCOLHA UMA OPÇÃO:

[1] Opção 1
[2] Opção 2
[3] Opção 3
""")

match operacao:
    case '1':
        print("Opção 1 foi escolhida...")
    case '2':
        print("Opção 2 foi escolhida...")
    case '3':
        print("Opção 3 foi escolhida...")
    case _:
        print("Opção inválida...")
