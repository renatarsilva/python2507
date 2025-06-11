# DESAFIO 06 v2

termo = int(input("Digite o termo: "))
razao = int(input("Digite a razão: "))
print(f"\nOs números da sua PA são: ", end=' ')
for i in range(termo, termo+razao*10, razao):    
    print(i, end=' ')    