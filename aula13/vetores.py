#fazer um programa que leia 2 vetors em 3 posições que representam forças sobre espaço 3D e escreva força resultante


f1 = []
f1.append (float (input("Insira valor do vetor de x em A: ")))
f1.append (float (input("Insira valor do vetor de y em A: ")))
f1.append (float (input("Insira valor do vetor de z em A: ")))

f2 = []
f2.append (float (input("Insira valor do vetor de x em B: ")))
f2.append (float (input("Insira valor do vetor de y em B: ")))
f2.append (float (input("Insira valor do vetor de z em B: ")))

#força resultante = (x1 + x2), (y1 + y2), (z1 + z2)

ft = []
ft.append (f1[0]+f2[0])
ft.append (f1[1]+f2[1])
ft.append (f1[2]+f2[2])

print (f"X: {ft[0]}, Y:  {ft[1]}, Z:  {ft[2]}")