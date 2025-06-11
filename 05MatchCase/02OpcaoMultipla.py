# OPÇÃO MULTIPLA

operacao = input("""
ESCOLHA UMA OPÇÃO:

[1] Opção 1
[2] Opção 2
[3] Opção 3
""")

match operacao:
    case '1' | '2':
        print("Opção 1 ou 2 escolhida...")
    case '3':
        print("Opção 3 foi escolhida...")
    case _:
        print("Opção inválida...")