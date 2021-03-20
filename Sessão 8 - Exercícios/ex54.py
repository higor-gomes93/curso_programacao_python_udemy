'''
Faça uma função que receba, por parâmetro, uma matriz A[4][4] e retorna a soma dos seus elementos.
'''

import random as r

matriz = []
vetor = []
linhas = 4
colunas = 4

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
            soma += parametro[i][j]
    print(soma)
    return

chama_matriz(matriz)
