# EXEMPLO 09

estado = {}
brasil = []

for _ in range(2):
    estado['uf']    = input("Digite a unidade federativa: ")
    estado['sigla'] = input("Digite a sigla do estado: ")
    brasil.append(estado.copy())

print(brasil)
print(brasil[0]['sigla'])