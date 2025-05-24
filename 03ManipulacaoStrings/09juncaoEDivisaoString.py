# JUNÇÃO E DIVISÃO DE STRINGS

texto = "SENAI Ary Torres"

# juntar caracteres com delimitador
print('.'.join(texto))

# dividir palavras em lista
print(texto.split())
print(texto.split()[0])   # primeira palavra
print(texto.split()[-1])  # última palavra
print(texto.split()[1])

lista = texto.split()
print(', '.join(lista))