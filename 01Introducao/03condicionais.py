#CONDICIONAIS

nota = float(input("Digite a nota1:"))
frequencia = int(input("Digite frequencia:"))

if nota > 6 and frequencia >= 75:
    print('aprovado')
else:
    print('Reprovado')

# DIAGRAMA MÉDIA

nota1: float = 0
nota2: float = 0
media = 0

nome: str = 'maki'

nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))

media = (nota1 + nota2)/2

if media >= 5:
    print("Aprovado")
else:
    print("Reprovado")

# DIAGRAMA MÉDIA

nota1 = 0
nota2 = 0
media = 0

nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))

media = (nota1 + nota2)/2

print("Aprovado" if media >= 5 else "Reprovado")

# EXEMPLO 01


nota = 49
ausencia = 15


if nota >= 50 and ausencia <= 15:
    print("Aprovado")
else:
    print("Reprovado")