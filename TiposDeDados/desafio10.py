
# # DESAFIO 10
# Imprima uma árvore de Natal como no exemplo utilizando a multiplicação
# de Strings.

#           *
#          ***
#         *****
#        *******
#       *********
#      ***********
#     *************
#    ***************
#   *****************
#          ***
#          ***
#          ***
# """

star = "*"
space = " "

print(f'\033[33m{space*11+star}')
print(f'\033[32m{space*10+star*3}')
print(f'{space*9+star*5}')
print(f'{space*8+star*7}')
print(f'{space*7+star*9}')
print(f'{space*6+star*11}')
print(f'{space*5+star*13}')
print(f'{space*4+star*15}')
print(f'{space*3+star*17}\033[')
print(f'\033[31m{space*10+star*3}')
print(f'{space*10+star*3}')
print(f'{space*10+star*3}\033[')
print("       🎁🎁🎁🎁")

