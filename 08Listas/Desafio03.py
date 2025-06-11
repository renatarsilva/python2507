# DESAFIO 03
"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
# DESAFIO 03
"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista_num2 = []
i = 1
while True:
    n = int(input(f"Digite o {i}º número (0 para sair): "))
    if n == 0:
        break
    lista_num2.append(n)
    i += 1


print(f"\n{len(lista_num2)} números digitados para a lista.")


print("Seus números em ordem decrescente: \n")
lista_num2.sort()
lista_num2.reverse()
for i in lista_num2:
    print(i, end=' ')


print()
print(f"\n{lista_num2.count(5)}x o 5 foi encontrado"
      if 5 in lista_num2 else
      "Não foi digitado o nº 5")

