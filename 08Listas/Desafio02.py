# DESAFIO 02
"""
Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já exista
lá dentro, ele não será adicionado. No final serão exibidos
todos os valores únicos digitados, em ordem crescente.
"""
lista_num = []
i = 1
while True:
    n = int(input(f"Digite o {i}º número (0 para sair): "))
    if n == 0:
        break
    if n not in lista_num:
        lista_num.append(n)
        i += 1
    else:
        print(f"\033[31mNúmero {n} já cadastrado!\033[0m")


print("Seus números em ordem crescente: \n")
lista_num.sort()
for i in lista_num:
    print(i, end=' ')