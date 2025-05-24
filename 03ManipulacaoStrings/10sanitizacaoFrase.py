# EXEMPLO DE SANITIZAÇÃO DE FRASE

frase2 = "   oi    SENAI   Ary Torres oi  ".strip()

frase2 = frase2.strip('oi')
frase2 = frase2.split()
frase2 = ' '.join(frase2)
print(frase2)