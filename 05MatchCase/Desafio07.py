# DESAFIO 07
"""
Escreva um programa que converta valores entre diferentes moedas.
O usuário deve inserir o valor em reais e selecionar a moeda para conversão:
D (Dólar), E (Euro), ou L (Libra). Utilize match case para aplicar a conversão
correta com base nas taxas fictícias fornecidas a seguir:


1 Real = 0.18 Dólar
1 Real = 0.16 Euro
1 Real = 0.13 Libra


Símbolos: $ € £
"""
real = float(input("Digite o valor: R$ "))
conversao = input("[D]Dolar [E]Euro [L]Libra: ").upper()


match conversao:
    case 'D':
        print(real*0.18)
    case 'E':
        print(real*0.16)
    case 'L':
        print(real*0.13)
    case _:
        print("Conversão inválida!")
