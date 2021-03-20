'''
Faça uma função que receba, por parâmetro, uma matriz A[7][6] e uma coluna N e retorne a soma dos elementos dessa
coluna.
'''

import random as r

matriz = []
vetor = []
linhas = 7
colunas = 6

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

def chama_matriz(parametro, coluna_n):
    soma = 0
    for i in range(linhas):
        for j in range(colunas):
            if j == coluna_n-1:
                soma += parametro[i][j]
    print(soma)
    return

chama_matriz(matriz, 3)
