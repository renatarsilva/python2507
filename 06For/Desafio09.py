# DESAFIO 09 (Utilização de operador ternário)
"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final  do programa mostre:
    A média de idade do grupo
    Qual é o nome do homem mais velho
    Quantas mulheres têm menos de 20 anos
"""

somaIdade = 0
nomeHomem = ""
hMaisVelho = float('-inf')
mulherMenos20 = 0

for i in range(1,5):
    nome = input(f"Digite o {i} nome: ")
    idade = int(input(f"Digite a {i} idade: "))
    sexo = input(f"Digite {i} sexo: (M/F) ").upper()

    somaIdade+=idade

    if sexo =='M' and idade > hMaisVelho:
        nomeHomem = nome
        hMaisVelho = idade
    if sexo == 'F' and idade < 20:
        mulherMenos20 += 1

media = somaIdade/4

print(f"\n\nA média de idade do grupo é: {int(media)} anos. ")
print(f"Homem mais velho: {hMaisVelho}")
print(f"Nenhuma mulher menos 20 cadastrada." if mulherMenos20 == 0 else
      f"{mulherMenos20} mulhe (es) tem menos de 20 anos.")
