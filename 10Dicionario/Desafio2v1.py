# DESAFIO 02 v1 (com busca por nome)

cont = 0
pessoa = input("Digite o nome da pessoa: ")
for i in range(len(almoco)):
    if pessoa.lower() == almoco[i]['nome'].lower():
        cont += 1
        print(f"{almoco[i]['nome']} come {almoco[i]['comida']} e bebe {almoco[i]['bebida']}")
if cont == 0:
    print("\nNenhum registro encontrado...")