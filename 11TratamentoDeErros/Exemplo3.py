# EXEMPLO 03

try:
    nota1 = float(input("Digite a 1ª nota: "))
    nota2 = float(input("Digite a 2ª nota: "))
    media = (nota1+nota2)/2
except:
    print("Deu ruim")
else:
    if media < 5:
        print(f"\nMédia: {media:,.1f}")
        print("Resultado: REPROVADO")
    elif media < 7:
        print(f"\nMédia: {media:,.1f}")
        print("Resultado: RECUPERAÇÃO")
    else:
        print(f"\nMédia: {media:,.1f}")
        print("Resultado: APROVADO")
