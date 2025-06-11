# EXEMPLO 12

for i in range(0, 11):
    for j in range(0, 11):
        print(f"{i+j}".rjust(3), end=' ')
    print()