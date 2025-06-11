# DESAFIO 06 v2

anterior = 0
atual    = 1
fibo     = 0
i        = 1
seqFibo  = '0 1 '
numero   = int(input("Digite uma quantidade para sequência Fibonacci: "))
while i <= numero-2:
    fibo     = anterior+atual
    seqFibo += f'{fibo} '
    anterior = atual
    atual    = fibo
    i+=1

print(seqFibo)