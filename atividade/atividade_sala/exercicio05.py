numeros = []


print("Digite 5 números inteiros")

for i in range(6):
    num = int(input(f"Qual é o {i + 1 }° numero: "))
    numeros.append(num)

x = int(input("Qual numros quer informação? "))

qtd = numeros.count(x)

print(f"O número {x} aparece {qtd} vezes na lista.")

indice_encontrado = -1
for i in range(6):
    if numeros[i] == x:
        indice_encontrado = i
        break

if indice_encontrado != -1:
    print(f"A primeira vez que que {x} aparece na lista é no indice: {indice_encontrado} !")
else:
    print(f"O número {x} não aparece na lista!")