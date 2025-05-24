# DESAFIO 08
"""
Solicite ao usuário o valor do salário atual, em seguida solicite o
percentual de aumento e imprima o valor do salário atualizado.
"""
salario = float(input("Digite o salario atual: "))
percentual = float(input("Digite o percentual: "))

print(f'O novo salário é {salario + salario * (percentual/100):,.2f}')