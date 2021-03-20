'''
Faça uma função que receba uma matriz 4 x 4 e retorne quantos valores maiores do que 10 ela possui.
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

def matriz_call(*args):
    cont = 0
    lista = list(args)
    for i in range(linhas):
        for j in range(colunas):
            if lista[i][j] > 10:
                cont += 1
    print(cont)
    return

def matriz_call2(matriz):
    cont = 0
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] > 10:
                cont += 1
    print(cont)
    return

matriz_call(*matriz)
matriz_call2(matriz)
