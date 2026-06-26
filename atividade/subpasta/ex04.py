def exibir_cabecalho (texto):
    tamanho = len(texto)
    print ("*" * tamanho)
    print(texto)
    print ("*" * tamanho)

frase = input("Insira uma frase: ")
print("gerando cabeçalho")
exibir_cabecalho(frase)