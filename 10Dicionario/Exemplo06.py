# EXEMPLO 06 (Alterar valores do dicionário)

almoco['bebida'] = 'Suco de laranja'
for chave, valor in almoco.items():
    print(f"{chave:12} | {valor:>15}")