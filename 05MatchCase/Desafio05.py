# DESAFIO 05
"""
Crie um programa que peça ao usuário para inserir uma letra. O programa deve utilizar match case
para verificar se a letra é uma vogal.
"""
letra = input("Digite uma letra: ").lower()
match letra:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print("\n\033[32mÉ uma vogal.")
    case _:
        print('\n\033[31mNão é uma vogal.')