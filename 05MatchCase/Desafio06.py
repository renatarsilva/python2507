# DESAFIO 06
"""
Crie um programa que peça ao usuário para inserir uma letra. O programa deve utilizar match case
para verificar se a letra é uma vogal (a, e, i, o, u) ou uma consoante, e então exibir uma mensagem apropriada.
"""
letra = input("Digite uma letra: ").lower()
match letra:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print("\n\033[32mÉ uma vogal.")
    case _ if letra.isalpha():
        print("\n\033[32mÉ uma consoante.")
    case _ if letra.isnumeric():
        print("\n\033[32mÉ um número inteiro.")
    case _:
        print('\n\033[31mÉ um caractere especial.')