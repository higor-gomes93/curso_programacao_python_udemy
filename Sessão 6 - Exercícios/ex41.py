'''
Faça um programa que calcule a associação em paralelo de dois resistores R1 e R2 fornecidos pelo
usuário via teclado. O programa fica pedindo estes valores e calculando até que o usuário entre
com um valor para resistência igual a zero.
'''
R1 = float(input("Insira o valor de R1: "))
R2 = float(input("Insira o valor de R2: "))

while R1 or R2 > 0:
    R = round((R1*R2)/(R1+R2),2)
    print(f"O valor da resistência equivalente é {R}.")
    R1 = float(input("Insira o valor de R1: "))
    R2 = float(input("Insira o valor de R2: "))
