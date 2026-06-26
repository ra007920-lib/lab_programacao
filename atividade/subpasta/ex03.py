def permitir_acesso(ano):
    idade = 2026 - ano
    if idade >= 18:
        return("Você é maior de idade")
    else:
        return("você é menor de idade")

print("Você é maior de idade?")
nascimento = int(input("Insira o ano em que você nasceu: "))

print(f"Status: {permitir_acesso(nascimento)}")
