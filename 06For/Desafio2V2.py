# DESAFIO 02 v2

soma = 0
cont = 0
for i in range(0, 501, 3):
    if i%2 != 0:
        soma+=i
        cont+=1
        print(f"{i:>5}", end=' ')
        if cont == 10:
            cont = 0
            print()

print(f"\n\n\033[1;4;33;40m Total: {soma:,} ".replace(',', '.'))