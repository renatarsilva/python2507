# DESAFIO 03 v1

tab = int(input("Digite um número: "))
print()
for i in range(1, 11):
    print(f"{tab:>3}  x {i:>3}  = \033[1;33m{tab*i:>3}\033[0m")