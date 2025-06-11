# DESAFIO 04
"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os
valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""
lista_geral = []
lista_par = []
lista_impar = []
i = 1
while True:
    x = int(input(f"Digite o {i}º número (0 para sair): "))
    if x == 0:
        break
    lista_geral.append(x)
    i += 1
    if x%2 == 0:
        lista_par.append(x)
    else:
        lista_impar.append(x)


print("\nLista geral:", lista_geral)
print("\nLista par:", lista_par)
print("\nLista ímpar:", lista_impar)
