#criar programa que leia um número do teclado e verifique se ele está dentro do intervalo entre 10 e 50(inclusive).
#se estiver, exibir "Dado válido", caso contrário, "Dado inválido". 
#loop para o programa, 0 para sair.
while True:
    valor = int(input("Insira um valor para verificar se está dentro da área (insira 0 para sair): "))
    if valor == 0:
        break
    else:
        if 10 <= valor <= 50:
            print("Dado válido")
        else:
            print("Dado inválido!")