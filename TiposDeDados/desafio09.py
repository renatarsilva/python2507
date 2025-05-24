# DESAFIO 09
"""
Crie um programa e declare uma constante PI utilizando 4 casas
decimais. Dados o raio e a altura, calcule e apresente o volume de um
objeto cilíndrico.
Fórmula: volume = PI * r² * altura
"""
PI = 3.1415
raio = float(input("Digite o raio:"))
altura = float(input("Digite a altura:"))
volume = round(PI * raio**2 * altura, 1)
print(f"O volume é: {volume:,} cm³")