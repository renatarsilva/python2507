# EXEMPLO 04

import time
from google.colab import output

while True:
    try:
        nota1 = float(input("Digite a 1ª nota: "))
        nota2 = float(input("Digite a 2ª nota: "))
        media = (nota1+nota2)/2
    except:
        output.clear()
        print("Deu ruim")
        time.sleep(3)
        print()
        continue
    else:
        if media < 5:
            print(f"\nMédia: {media:,.1f}")
            print("Resultado: REPROVADO")
        elif media < 7:
            print(f"\nMédia: {media:,.1f}")
            print("Resultado: RECUPERAÇÃO")
        else:
            print(f"\nMédia: {media:,.1f}")
            print("Resultado: APROVADO")
        break

