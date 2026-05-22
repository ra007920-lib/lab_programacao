vetor = []
soma = 0
numero = int(input("Insira a quantidade de números que você gostaria de encontrar a média: "))

for i in range (numero):
    valor = float(input("Insira o valor: "))
    vetor.append(valor)

soma = sum(vetor)
media = soma / numero
alvo = vetor[0]

if vetor[0] > media:
    menor = vetor[0] - media
else:
    menor = media - vetor[0]

for i in range(numero):
    if vetor[i] > media:
        distatual = vetor[i] - media
    else:
        distatual = media - vetor[i]
    if distatual < menor:
        menor = distatual
        alvo = vetor[i]

print ("Valores:")
print(vetor)
print("-"*30)
print(f"Média: {media:.2f}")
print("-"*30)
print(f"Valor mais próximo da média: {alvo}")
