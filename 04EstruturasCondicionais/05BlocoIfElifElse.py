#Bloco if elif else

temp = (int(input("Digite a temperatura de 0 a 40: ")))

if temp < 0 or temp > 40:
    print("Valor inválido")
    exit()

    if temp < 10:
        print("Frio")
elif temp <20:
    print("Morno")
elif temp <30:
    print("Quente")
else:
    print("Muito quente")    