# EXEMPLO 07
""" continue pula a iteração """

lista = [1, 10, 20, 30, 40, 50]

for numero in lista:
    if numero == 30:
        continue
    print(numero, end=' ')