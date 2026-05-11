#fazer um programa que preencha por leitura um vetor de 5 posições, e informe a posição em que um valor x (lido no teclado) aparece pela ultima vez no vetor. 
#caso o valor x não seja encontrado, o programa retorna o valor -1.
#primeiro, criar lista para vetor
vetor = []
#agora a repetição para preencher por leitura 5 posições do vetor
for i in range (5):
    numero = int(input("Digite um vetor: "))
    vetor.append(numero)
#agora o programa irá ler o valor x que queremos encontrar a posição
x = int(input("Digite o valor x que deseja encontrar: "))
#agora o programa irá verificar a posição em que o valor x aparece pela ultima vez no vetor
ultima_posicao = -1
for i in range(len(vetor)):
    if vetor[i] == x:
        ultima_posicao = i
#agora o programa irá verificar se o valor x foi encontrado ou não
if ultima_posicao != -1:
    print(f"O valor x aparece pela ultima vez na posição: {ultima_posicao}")
else:
    print("Valor não encontrado (-1)")
