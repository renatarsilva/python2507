# ANÁLISE DE STRINGS

frase = "SENAI Ary Torres"

# tamanho da string
print(len(frase))

# contar caracteres
print(frase.count('r'))

# encontrar índice (retorna -1 se não encontrar)
print(frase.find('z'))

# encontrar índice (a partir da direita)
print(frase.rfind('s'))

# encontrar índice (gera erro se não encontrar)
print(frase.index('r'))

# verificar pertinência
print('Ary' in frase)