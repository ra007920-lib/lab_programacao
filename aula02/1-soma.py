#interpretar e converter pseudocódigo em código python
#leia = entrada
# <- = adicionar valor à variável
# escreva = print
'''pseudocódigo:
Leia A
Leia B
soma <- A+B
escreva soma'''
#1.  leia A (Convertendo para int)
A= int(input("Escreva o valor de A: "))
#2.  leia B (Convertendo para int)
B = int(input("Escreva o valor de B: "))
#3. realiza a soma dos dois valores A e B
soma = A + B
#4. imprime para o usuário
print(f"O resultado da soma é: {soma}")