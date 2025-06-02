#Desafio1

bairro = input("Digite o bairro:")

if bairro.upper().split()[0] == "SANTO":
    print(f"O bairro {bairro.title()} começa com santo")
else:
    print(f"O bairro {bairro.title()} não comeca com santo")    