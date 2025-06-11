# DESAFIO 02 v1

soma = 0

for n in range(3, 501, 3):
    if n%2 != 0:
        soma += n

print(f"Resultado da soma: {soma:,}".replace(',', '.'))