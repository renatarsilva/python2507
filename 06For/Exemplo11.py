# EXEMPLO 11

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j}".rjust(3), end=' ')
    print()