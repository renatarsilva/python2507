# MÉTODOS PARA LISTAS


lista = [4, 5, 3, 5]
print(lista)


# ADICIONAR ITENS A LISTA
lista.append(2)
print(lista)


# ADICIONAR VALOR NO ÍNDICE ESPECÍFICO
lista.insert(2, -3)
print(lista)


# CONTAR VALORES
print(lista.count(5))


# VERIFICAR TAMANHO DA LISTA
print(len(lista))


# OBTER ÍNDICE DO ITEM DA LISTA
print(lista.index(5))


# REVERTER ITENS DA LISTA
lista.reverse() # Não atribuir a uma variável
print(lista)


# ORDENAR A LISTA
lista.sort() # Não atribuir a uma variável
print(lista)


# REMOVER ITEM ATRAVÉS DO VALOR
lista.remove(5)
print(lista)


# REMOVER ÚLTIMO ITEM DA LISTA (recebe valor removido)
removeu = lista.pop()
print(removeu)
print(lista)


# REMOVER INTERVALO OU ÍNDICE
del lista[1:3]
print(lista)


# LIMPAR LISTA
lista.clear()
print(lista)