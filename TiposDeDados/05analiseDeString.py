# ANÁLISE DE STRINGS (str)

n = '5'

print(n.isnumeric())   # Númérico
print(n.isalpha())     # Alfabético
print(n.isalnum())     # Alfanumérico
print(n.isupper())     # Maiúscula
print(n.islower())     # Minúscula
print(n.istitle())     # Primeira maiúscula
print(n.isdecimal())   # Numérico
print(n.isspace())     # Espaço

# EXEMPLO

num = input("Digite um número: ")
if num.isnumeric():
    num = int(num)
else:
    print("Não é número!")

# print(type(num))