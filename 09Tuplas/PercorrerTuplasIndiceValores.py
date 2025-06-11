# PERCORRER UMA TUPLA POR ÍNDICE E VALORES

lanches = ('Hamburger', 'Pastel', 'Coxinha', 'Pizza')

for posicao, lanche in enumerate(lanches):
    print(f"{posicao+1} | {lanche}")