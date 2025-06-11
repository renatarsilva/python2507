# DESAFIO 02 v2

import random

pc = random.randint(1, 10)
palpites = 1

while True:
    pl = int(input("Adivinhe o número que o computador pensou (1 a 10):  "))
    if pl == pc:
        print(f"\n\033[32mParabéns, você adivinhou com {palpites} palpite(s).\n\033[0m😄")
        break
    else:
        print("\n\033[31mErrou!\n\033[0m😒")
        palpites += 1