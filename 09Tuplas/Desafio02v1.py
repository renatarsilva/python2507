# DESAFIO 02 v1

import random

tupla = tuple(random.randint(1, 50) for i in range(5))

print(f"Tupla: {tupla}")
print(f"Maior valor: {max(tupla)}")
print(f"Menor valor: {min(tupla)}")