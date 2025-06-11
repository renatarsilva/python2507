# DESAFIO 07 v1

dolar = 0.18
euro = 0.16
libra = 0.13

print("""
___________________________

🤑\033[1;32m  CONVERSÃO DE MOEDAS \033[0m 💲
___________________________
""")

valor = float(input("Digite um valor em R$ para conversão: \n\n"))
conversao = input("\nEscolha a moeda: D (Dólar) E (Euro) L (Libra) \n\n").lower()

match conversao:
    case 'd':
        print(f"\n$ {(valor*dolar):,.2f}")
    case 'e':
        print(f"\n€ {(valor*euro):,.2f}")
    case 'l':
        print(f"\n£ {(valor*libra):,.2f}")
    case _:
        print("\n\033[31mConversão inválida...")