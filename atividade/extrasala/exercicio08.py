
vetor = []
palavra = ""
frase = input("Digite uma frase curta separada por espaços: ")

for carac in frase:
    if carac == " ":
        if palavra != "":
            vetor.append(palavra)
            palavra = ""
    else:
        palavra += carac
        
if palavra != "":
    vetor.append(palavra)

print("\nResultado do split manual:")
print(vetor)