# DESAFIO 06 v1

termo = int(input("Digite o termo: "))
razao = int(input("Digite a razão: "))
print("\nOs números da sua PA são: ", end=' ')
for i in range(10):    
    print(termo, end=' ')
    termo += razao
