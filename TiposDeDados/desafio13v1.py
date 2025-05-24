# DESAFIO 13 V1
"""
Com base no DESAFIO 12, faça com que o usuário digite
um produto e um valor para acrescentar no cardápio.
"""
produto = input("Digite o produto: ")
valor = 'R$ '+input("Digite o valor R$: ")
print()
print('\033[1;33;42m'," CARDÁPIO ".center(40, '#'),'\033[0m\n')


print(f"{'Pastel'.ljust(32, '.')}{'R$ 6,50'.rjust(10, '.')}")
print(f"{'Coxinha'.ljust(32, '.')}{'R$ 16,50'.rjust(10, '.')}")
print(f"{'Risoles de queijo'.ljust(32, '.')}{'R$ 156,50'.rjust(10, '.')}")
print(f"{produto.ljust(32, '.')}{valor.rjust(10, '.')}")