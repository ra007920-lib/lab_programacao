#separador par impar dinamico
#elabore um programa que leia 10 numeros inteiros do teclado. à medida que os números forem lidos, os pares devem ser inseridos em uma lista chamada pares e impares na lista impares. Porém, se o usuario digitar um número que já foi inserido anteriormente, o programa deve recusar e pedir outro
impar = []
par = []

while len(par) + len(impar) < 10:
    posicao = len(par) + len(impar) + 1
    num = int(input(f"Insira o {posicao}º valor: "))

    if num in par or num in impar:
        print("Esse número já foi inserido anteriormente! Tente novamente.")
        continue 
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print("-" * 30)
print(f"Lista de Pares: {par}")
print(f"Lista de Ímpares: {impar}")