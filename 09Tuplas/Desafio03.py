# DESAFIO 03
"""
Desenvolva um programa que leia quatro números inteiros pelo teclado e guarde-os em uma tupla. No final, mostre:
    A) Quantas vezes apareceu o valor 9.
    B) Em que posição foi digitado o primeiro valor 3.
    C) Quais foram os números pares.
"""
tupla_numeros = tuple(int(input(f"Digite o {i}º número: ")) for i in range(1, 5))

print(f"\nO número 9 apareceu {tupla_numeros.count(9)} vez(es)" if 9 in tupla_numeros else "\nNão foi digitado o nº 9")
print(f"O nº 3 apareceu 1º na {tupla_numeros.index(3)+1}ª posição" if 3 in tupla_numeros else "Não foi digitado o nº 3")
print("Números pares: ", end=' ')
cont=0
for num in tupla_numeros:
    if num%2 == 0:
        print(num, end=' ')
        cont+=1
if cont==0:
    print("\033[31mNenhum número par foi digitado\033[0m")