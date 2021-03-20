'''
Leia duas matrizes 4 x 4 e escreva uma terceira matriz com os maiores valores de cada posição das matrizes lidas.
'''

import random as r

matriz_1 = []
matriz_2 = []
matriz = []
vetor = []
linhas = 4
colunas = 4

for i in range(linhas):
    for j in range(colunas):
        num = r.randrange(0, 50)
        vetor.append(num)
    matriz_1.append(vetor)
    vetor = []

for i in range(linhas):
    for j in range(colunas):
        num = r.randrange(0, 50)
        vetor.append(num)
    matriz_2.append(vetor)
    vetor = []

for i in range(linhas):
    for j in range(colunas):
        if matriz_1[i][j] > matriz_2[i][j]:
            num = matriz_1[i][j]
            vetor.append(num)
        elif matriz_1[i][j] < matriz_2[i][j]:
            num = matriz_2[i][j]
            vetor.append(num)
        else:
            num = matriz_1[i][j]
            vetor.append(num)
    matriz.append(vetor)
    vetor = []

for i in range(linhas):
    for j in range(colunas):
        print(f'{matriz_1[i][j]:^3}', end = ' ')
    print()

for i in range(linhas):
    for j in range(colunas):
        print(f'{matriz_2[i][j]:^3}', end = ' ')
    print()

for i in range(linhas):
    for j in range(colunas):
        print(f'{matriz[i][j]:^3}', end = ' ')
    print()
