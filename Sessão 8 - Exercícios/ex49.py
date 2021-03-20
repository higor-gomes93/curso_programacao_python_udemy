'''
Faça uma função que receba uma matriz de 3 x 3 elementos. Calcule e retorne a soma dos elementos que estão abaixo
da diagonal principal.
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

def chama_matriz(*args):
    soma = 0
    for i in range(linhas):
        for j in range(colunas):
            if i > j:
                soma += args[i][j]
    print(soma)
    return

chama_matriz(*matriz)
