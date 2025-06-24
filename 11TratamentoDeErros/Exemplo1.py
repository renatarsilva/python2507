# EXEMPLO 01

try:
    numerador   = int(input("Digite o numerador: "))
    denominador = int(input("Digite o denominador: "))
    razao = numerador/denominador
except Exception as erro:
    print(f"Erro encontrado: {erro}")
    print(f"Erro encontrado: {erro.__class__}")
else:
    print(razao)