# EXEMPLO 01

compras = [10.2, 3.35, 16.3, ['Tomate', 'Cebola', 'Pimentão']]

print(f"O {compras[3][0]} custa R$ {compras[0]:,.2f}")
print(f"A {compras[3][1]} custa R$ {compras[1]:,.2f}")
print(f"O {compras[3][2]} custa R$ {compras[2]:,.2f}")

print(f"\nValor Total: R$ {compras[0]+compras[1]+compras[2]:,.2f}")