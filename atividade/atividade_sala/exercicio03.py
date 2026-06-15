palavra = input("Digite uma palvra: ").lower()
vogais = 0

for letra in palavra:
    if letra in "aeiou":
        vogais += 1

print(f"A palvra {palavra} tem {vogais} vogais.")
