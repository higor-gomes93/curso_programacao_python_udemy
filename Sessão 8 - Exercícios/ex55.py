'''
Faça uma função que receba, por parâmetro, uma matriz A[3][3] e retorna a soma dos seus elementos da sua diagonal
principal e da sua diagonal secundária.
'''

import random as r

matriz = []
vetor = []
linhas = 3
colunas = 3

for i in range(linhas):
    for j in range(colunas):
        num = r.randrange(1, 21)
        vetor.append(num)
    matriz.append(vetor)
    vetor = []

for i in range(linhas):
    for j in range(colunas):
        print(f'{matriz[i][j]:^2}', end = ' ')
    print()

print()

def chama_matriz(parametro):
    soma = 0
    for i in range(linhas):
        for j in range(colunas):
            if i == j or i + j == 2:
                soma += parametro[i][j]
    print(soma)
    return

chama_matriz(matriz)
