'''
Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado
Triângulo de Floyd.
'''

num = int(input("Insira um valor n: "))
cont = 0

for i in range(1, num+1):
    for j in range(1, 1+i):
        cont += 1
        print(cont, end = ' ')
    print("\n")
