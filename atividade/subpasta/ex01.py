def nota_aluno(nota1,nota2):
    media = (nota1+ nota2)/2
    print(media)
    if media > 6:
        print("Aprovado")
    elif 6 > media > 4:
        print("Verificação Suplementar")
    else:
        print("Reprovado")
    

nome = input("Insira a nota do aluno: ")
notaA = float(input(f"Insira a primeira nota de {nome}: "))
notaB = float(input(f"Insira a segunda nota de {nome}: "))

nota_aluno(notaA,notaB)
