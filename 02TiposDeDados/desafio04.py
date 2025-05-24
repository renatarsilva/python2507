# DESAFIO 04
"""
Crie um programa para entrar com a base e a altura de um retângulo e imprimir
respectivamente o perímetro e a área correspondente.
"""
base = float(input())
altura = float(input())
area = base * altura
perimetro =  2 * (base + altura)
print(f'A area do retangulo é {area}, e o perimetro é {perimetro}')
