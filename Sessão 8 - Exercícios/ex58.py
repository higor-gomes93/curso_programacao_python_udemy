'''
Faça uma função que receba, por parâmetro, duas matrizes quadradas de ordem N, A e B, e retorne uma matriz C,
também por parâmetro, que seja o produto matricial de A e B.
'''

import random as r

matriz_1 = []
matriz_2 = []
vetor = []
ordem = 3

for i in range(ordem):
    for j in range(ordem):
        num = r.randrange(1, ordem**2 +1)
        vetor.append(num)
    matriz_1.append(vetor)
    vetor = []

for i in range(ordem):
    for j in range(ordem):
        print(f'{matriz_1[i][j]:^2}', end = ' ')
    print()

print()

for i in range(ordem):
    for j in range(ordem):
        num = r.randrange(1, ordem**2 +1)
        vetor.append(num)
    matriz_2.append(vetor)
    vetor = []

for i in range(ordem):
    for j in range(ordem):
        print(f'{matriz_2[i][j]:^2}', end = ' ')
    print()

print()

def produto_matricial(A, B):
    matriz_produto = []
    vetor = []
    
    for i in range(ordem):
        for j in range(ordem):
            num = A[i][j]*B[j][i]
            vetor.append(num)
        matriz_produto.append(vetor)
        vetor = []
    
    for i in range(ordem):
        for j in range(ordem):
            print(f'{matriz_produto[i][j]:^2}', end = ' ')
        print()
    return

produto_matricial(matriz_1, matriz_2)
