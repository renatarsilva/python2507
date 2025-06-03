# DESAFIO 18
"""
Desenvolva uma lógica que leia o peso e a altura de uma
pessoa, calcule seu IMC e mostre seu status, de acordo com a
tabela abaixo:


Abaixo de 18.5: Abaixo do Peso
Entre 18.5 e 25: Peso ideal
Entre 25 e 30: Sobrepeso
Entre 30 e 40: Obesidade
Acima de 40: Obesidade Mórbida
"""

peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))
IMC = peso / (altura*altura)

if IMC < 18.5:
    print("Abaixo do Peso")
elif IMC < 25:
    print("Peso ideal")
elif IMC < 30:
    print("Sobrepeso")  
elif IMC <40:
    print("Obesidade")
else:
    print("Obesidade Mórbida")              
