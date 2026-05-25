vetor = []
soma = 0
numero = int(input("Insira a quantidade de números que você gostaria de encontrar a média: "))

for i in range (numero):
    valor = float(input("Insira o valor: "))
    vetor.append(valor)

media = soma / numero
alvo = vetor[0]

menor_distancia = abs(vetor[0] - media)
for i in range(numero):
    distancia_atual = abs(vetor[i] - media)
    if distancia_atual < menor_distancia:
        menor_distancia = distancia_atual
        alvo = vetor[i]

print ("Valores:")
print(vetor)
print("-"*30)
print(f"Média: {media:.2f}")
print("-"*30)
print(f"Valor mais próximo da média: {alvo}")
