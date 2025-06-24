# EXEMPLO 02

try:
    # Código que pode gerar erro
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except(ValueError, TypeError):
    # Trata erros mencionados acima
    print("Digite um número válido")
except(ZeroDivisionError):
    # Trata erro mencionado acima
    print("Não é possível dividir por zero")
else:
    # Executa se não houver erro
    print(f"\nResultado: {resultado}")
finally:
    # Sempre executa
    print("\nEncerrando o programa...")

