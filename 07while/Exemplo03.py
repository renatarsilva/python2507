# EXEMPLO 03

i=0
while i < 5:
    i+=1
    if i == 3:
        print("Pulando a iteração 3")
        continue
    print(i)
else:
    print("Fim do loop.")