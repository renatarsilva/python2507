# OPERADOR TERNÁRIO

import random
pc = random.randint(1, 3)
pl = int(input("Adivinhe o nº do computador (1 a 3): "))

print(pc)
print("\nVenceu! 😁" if pl == pc else "\nPerdeu! 😥")