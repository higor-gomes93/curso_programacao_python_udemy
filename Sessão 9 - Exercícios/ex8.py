'''
Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado Triângulo
de Pascal.
'''
num = 6

auxiliar = [[0 if 0 < j < i-1 else 1 for j in range(i)]for i in range(1, num+1)]

for i in range(2, num):
    for j in range(i):
        if 0 < j < i:
            auxiliar[i][j] = auxiliar[i-1][j] + auxiliar[i-1][j-1]

[print(*i) for i in auxiliar]
