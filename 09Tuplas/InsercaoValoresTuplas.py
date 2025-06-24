# Digitação pelo usuário
tupla = tuple(int(input(f"Digite o {i+1} nº: ")) for i in range(5))
print("\nDigitados pelo usuário:", tupla)


# Números aleatórios
import random
tupla = tuple(random.randint(1, 50) for i in range(5))
print("\nNúmeros aleatórios:", tupla)


# Contagem
tupla = tuple(i for i in range(1, 11))
print("\nContagem:", tupla)


# Valores condicionais
numeros = (4, 8, 7, 10, -50)
pares = tuple(num if num%2==0 else '' for num in numeros)
print("\nPares condicionais:", pares)


# Imprimir diretamente uma Tupla
print("\nNúmeros pares de 0 a 10:", tuple(i for i in range(0, 11, 2)))