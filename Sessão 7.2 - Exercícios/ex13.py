'''
Gere uma matriz 4 x 4 com valores no intervalo [1, 20]. Escreva um programa que transforme a matriz gerada numa
matriz triangular inferior, ou seja, atribuindo zero a todos os elementos acima da diagonal principal.
Imprima a matriz original e a matriz transformada.
'''

import random as r

matriz = []
vetor = []
linhas = 4
colunas = 4

for i in range(linhas):
    for j in range(colunas):
        num = r.randrange(1,21)
        vetor.append(num)
    matriz.append(vetor)
    vetor = []

for i in range(linhas):
    for j in range(colunas):
        if j > i:
            matriz[i][j] = 0
        print(f'{matriz[i][j]:^3}', end = ' ')
    print()
