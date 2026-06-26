numero = int(input("Digite um número inteiro positivo: "))
produto = 1

for i in range(1, numero + 1, 2):
    produto *= i

print(f"O produto dos ímpares ate {numero} é: {produto}")
