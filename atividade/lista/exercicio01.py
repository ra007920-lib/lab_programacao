import random

vetor1= []
vetor2 = [0,0,0,0,0,0]

for e in range (100):
    vetor1.append(random.randint(1,6))
for i in range (6):
    vetor2[i] = vetor1.count(i+1)
# vetor2[0] = vetor1.count(1)
# vetor2[1] = vetor1.count(2)
# vetor2[2] = vetor1.count(3)
# vetor2[3] = vetor1.count(4)
# vetor2[4] = vetor1.count(5)
# vetor2[5] = vetor1.count(6)
print("-"*30)
print("Resultado das jogadas:")
print(vetor1)
print("-"*30)
print("Quantidade de vezes que caiu cada face do dado:")
print(f"1: {vetor2[0]} | 2: {vetor2[1]} | 3: {vetor2[2]} | 4: {vetor2[3]} | 5: {vetor2[4]} | 6: {vetor2[5]} ")
