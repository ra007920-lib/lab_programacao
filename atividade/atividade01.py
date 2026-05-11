#fazer um programa que preencha por leitura um vetor de 10 posições, e conta quantos vetores diferentes existem no vetor.
#primeiro, criar lista para vetor
vetor = []
#precisamos preencher com uma repetição para que o usuario preencha 10 vezes o vetor.
for i in range (10):
    numero = int(input("Digite um vetor: "))
    vetor.append(numero)
#agora precisamos contar quantos vetores diferentes existem na lista.
set_vetor = set(vetor)
#o set irá eliminar vetores repetidos, então podemos contar quantos vetores difererntes sobraram
quantidade_diferentes = len(set_vetor)
print(f"A quantidade de vetores diferentes é: {quantidade_diferentes}")