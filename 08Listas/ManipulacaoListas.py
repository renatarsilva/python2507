# MANIPULAÇÃO DE LISTAS

bancos = ['Banco do Brasil', 'CEF', 'Santander']
print(bancos)
print(bancos[1])

# SUBSTITUIR ITEM DA LISTA
bancos[1] = 'Itaú'
print(bancos)

# SUBSTITUIR ÚLTIMO ITEM DA LISTA
bancos[-1] = 'C6'
print(bancos)

# AGREGAR ITENS A LISTA
bancos = bancos + ['Safra']
print(bancos)

# AGREGAR ITENS A LISTA (Operador de atribuição)
bancos += ['Bradesco', 'Nubank']
print(bancos)