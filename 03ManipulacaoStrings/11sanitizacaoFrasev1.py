# EXEMPLO DE SANITIZAÇÃO DE FRASE v1

frase2 = ' '.join("   oi    SENAI   Ary Torres oi  ".strip().strip('oi').split())

print(frase2)