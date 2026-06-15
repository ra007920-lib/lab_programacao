nomes = []

print("Digite 5 nomes: ")
for i in range(5):
    nome = input(f"Qual é o {i + 1}° nome: ")
    nomes.append(nome)

nomes_invertidos = [nomes[::-1]]

print(f"\nLista original: {nomes}")
print(f"Lista invertida: {nomes_invertidos}")