# EXEMPLO 05

while True:
    r = input("Digite (S) para sair ou (C) para continuar\n").upper()
    if r != 'S' and r != 'C':
        print("\nDeixa de besteira, só vale S e C! 👶")
        continue
    if r == 'S':
        print("Saindo do loop...")
        break
    print("\nContinuando...\n")