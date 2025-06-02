#Desafio2

nome = input("Digite seu nome completo: ")
verificaNome = nome.lower()

if 'silva' in verificaNome.split():
    print("Contém 'Silva'")
else: 
    print("Não contém 'Silva' ")