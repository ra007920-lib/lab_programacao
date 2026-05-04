#um dado é lançado 50x, o valor correspondente é armazenado em um vetor. O programa simula o lançamento do dado e determina o percentual de ocorrencias de face 6 do dado dentre 50 lançamentos.
#primeiro precisamos importar random
import random
#agora precisamos criar a lista vetor
vetor = []
#agora simulamos o lançamento de dado 50x
for i in range (50):
    numero = random.randint(1, 6)
    vetor.append(numero)
#agora o programa irá contar quantas vezes o 6 apareceu no vetor
contador = 0
for i in range(len(vetor)):
    if vetor[i] == 6:
        contador += 1
#agora faremos o cálculo percentual
percentual = (contador / 50) * 100
print(f"O percentual de ocorrencias de face 6 do dado dentre 50 lançamentos é: {percentual:.2f}%")