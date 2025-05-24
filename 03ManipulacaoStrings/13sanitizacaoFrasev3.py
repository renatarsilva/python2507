# EXEMPLO DE SANITIZAÇÃO DE FRASE v3

print(('').join("   endereco de EMAIL @gmail.com    ".strip().replace('@gmail.com', "@outlook.com").lower().split()))

email = 'makiemail@gmail.com'.split('@')[-1]
print(email)

email = 'makiemail@gmail.com'.split('@')[0]
print(email)

email = 'makiemail@gmail.com'.split('@')[1]
print(email)