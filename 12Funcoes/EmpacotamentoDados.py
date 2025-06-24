# EMPACOTAMENTO DE DADOS

def mult(*numeros):
    # print(type(numeros))
    calculo=1
    for i in numeros:
        calculo*=i
    return calculo

print(mult(2, 5, 100))