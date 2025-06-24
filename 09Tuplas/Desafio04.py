# DESAFIO 04
"""
Crie um programa que tenha uma tupla única com 4 produtos e seus respectivos preços em sequência.
Exiba uma listagem com os nomes e preços, organizando os dados em forma tabular.
"""
produtos = ('Camiseta', 50, 'Calça', 79, 'Bermuda', 40, 'Blusa', 100)

for i, item in enumerate(produtos):
    if i%2 ==0:
        print(f"{item}".ljust(20, '.'), end ='')
    else:
        print(f"R$ {item:,.2f}".replace('.', ',').rjust(10, '.'))s