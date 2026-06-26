# fluxo de caixa
positivo = []
negativo = []
somap = 0
soman = 0

while True:
    num = float(input("Digite um valor (positivo para receita, negativo para despesas). Digite 0 para sair: "))
    if num > 0:
        positivo.append(num)
        somap += num
    elif num < 0:
        negativo.append(num)
        soman += num
    elif num == 0:
        break
    
    print(f"Receita atual: {positivo}")
    print(f"Despesa atual: {negativo}\n")

print("\n--- Valores menores que R$ 5,00 serão deletados ---")
for valor in positivo[:]: 
    if valor < 5.00:
        positivo.remove(valor)

for valor in negativo[:]: 
    if valor > -5.00:
        negativo.remove(valor) 
total = somap + soman 

print(f"Receitas finais: {positivo}")
print(f"Despesas finais: {negativo}")
print(f"Balanço final: R$ {total:.2f}")