# REFATORAÇÃO DE CÓDIGO

# ORIGINAL
a = 10
b = 20
c = a+b
print('Original', c)

# REFATORADO
def soma(x, y):
    return x+y

print('Refatorado', soma(10, 20))