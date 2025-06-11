# EXEMPLO 06

# Bibliotec para limpar o console:
from google.colab import output
import time


while True:
    time.sleep(3)
    output.clear()
    r = input("Digite (S) para sair ou (C) para continuar\n").upper()
    if r != 'S' and r != 'C':
        print("\nDeixa de besteira, só vale S e C! 👶")
        continue
    if r == 'S':
        output.clear()
        print("Saindo do loop...")
        break
    print("\nContinuando...\n")