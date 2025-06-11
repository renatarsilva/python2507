# DESAFIO 01 v2

from google.colab import output
msg = True

while True:
    print("", end='' if msg else "Sexo inválido...")
    sexo = input("Digite o sexo: (M/F): ").upper()
    if sexo != 'M' and sexo != 'F':
        msg = False
        output.clear()
        continue
    output.clear()
    if sexo == 'M':
        print("\033[32mSexo M cadastrado com sucesso!\033[0m")
    else:
        print("\033[32mSexo F cadastrado com sucesso!\033[0m")
    break