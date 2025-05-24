# substituir palavras

frase = "SENAI Ary Torres"
print(frase.replace('SENAI', 'ESCOLA'))
print(frase)
frase = frase.replace('SENAI', 'ESCOLA')
print(frase)

frase2 = "   oi    SENAI   Ary Torres oi  "

# retirada/limpeza
print(frase2.strip())
frase2 = frase2.strip() # limpar espaços antes e depois

print(frase2.strip('oi'))

url = 'https://google.com/h'
print(url.rstrip('h'))

print(url.lstrip('https://'))