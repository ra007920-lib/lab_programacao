
notas = []
for i in range(5):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)

menor = notas[0]
indice_menor = 0

for i in range(1, len(notas)):
    if notas[i] < menor:
        menor = notas[i]
        indice_menor = i

notas_restantes = []
for i in range(len(notas)):
    if i != indice_menor:
        notas_restantes.append(notas[i])

print("\nNotas restantes:")
for nota in notas_restantes:
    print(nota)
