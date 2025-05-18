# Desafio troca de variaveis
a = 5
b = 2
c = 0

c = a
a = b
b = c

print(a, b)

# Desafio troca de variaveis (Modo simultaneo)
a = 5
b = 2

a , b = b, a

print(a, b)

nome = "Renata"
idade = 25
sexo = 'M'

nome, idade, sexo = idade, sexo, nome
print (nome, idade, sexo)

x = 2
y = 3
z = x * y + y
