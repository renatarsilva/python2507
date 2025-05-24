# DESAFIO 13
"""
Com base no DESAFIO 12, faça com que o usuário digite
um produto e um valor para acrescentar no cardápio.
"""

l01 = "1 - Burguer________R$7,90 🍔"
l02 = "2 - X-burguer______R$8,30 🍔"
l03 = "3 - X-egg__________R$8,50 🍔"
l04 = "4 - Refrigerante Guaraná R$2,50 🥃"
l05 = "5 - Coca-Cola______R$2,70"

print("\033[47m \033[35m",  "MENU".center(32,"-"), "\033[")

print(f"{l01}".ljust(22,'-'))
print(f"{l02}".ljust(22,'-'))
print(f"{l03}".ljust(22,'-'))
print(f"{l04}".ljust(22,'-'))
print(f"{l05}".ljust(22,'-'))
print("\033[47m \033[35m","-"*31, "\033[")

print("\n","\033[47m \033[35m Faça seu pedido aqui $$ \033[".center(44,"-"))

codigo = "N° do Pedido "+input("Digite o número do pedido ")
data = "Data " +input("Digite a data da compra ")

pedido = input("Digite o código do produto ")

if pedido == "1":
    comida = l01
elif pedido == "2":
    comida = l02
elif pedido == "3":
    comida = l03
elif pedido == "4":
    comida = l04
elif pedido == "5":
    comida = l05
else:
    print("Opção inválida! Tente novamente")

print(f"\n {codigo.center(32, '-')} \n{data.center(32, '-')}")
print(f"\n {comida}")
print("-"*31)

