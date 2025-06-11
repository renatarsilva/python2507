# VERIFICAR SE UMA LISTA POSSUI ITENS

letras = ['a', 'b', 'c', 'd', 'e', 'f']
letra = input("Digite a letra: ").lower()

if letra in letras:
    print("\033[32mEstá")
else:
    print("\033[31mNão está")