variavelGlobal = 5
numero = 500


def funcaoGlobal():
    global variavelGlobal, numero
    variavelGlobal += 1
    print(variavelGlobal, numero)


print(variavelGlobal)
funcaoGlobal()