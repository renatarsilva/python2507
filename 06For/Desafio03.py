# DESAFIO 03
"""
Mostre a tabuada de um número que o usuário escolher.
"""
tab = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{i} x {tab} = {i*tab}")