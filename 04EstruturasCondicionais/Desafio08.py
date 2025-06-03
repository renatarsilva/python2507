# DESAFIO 08
"""
Desenvolva um programa que pergunte a distância de uma
viagem em Km. Calcule o preço da passagem cobrando R$
0,50 por Km para viagens de até 200 Km e R$ 0,45 para
viagens mais longas.
"""

distancia = float(input("Digite o tamanho da distância em KM"))

if distancia > 200:
    print(f" O valor da viagem será R${distancia * 0.45}")
else:
    print(f"O valor da viagem será R${distancia * 0.50}")