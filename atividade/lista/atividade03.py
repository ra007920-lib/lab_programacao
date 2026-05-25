#programa que percorre duas listas e intercala os elementos de ambas, formando uma terceira lista.
lista1 = [1,2,3,4]
lista2 = [10,20,30,40,50,60]
lista3 = []


if len(lista1) <= len(lista2):
    menor = lista1
    maior = lista2

else:
    menor = lista2
    maior = lista1

for i in range(len(maior)):
    if (i < len(menor)):
        lista3.append(menor[i])
    lista3.append(maior[i])

print(f"lista1: {lista1}")
print(f"lista2: {lista2}")
print(f"lista intercalada: {lista3}")