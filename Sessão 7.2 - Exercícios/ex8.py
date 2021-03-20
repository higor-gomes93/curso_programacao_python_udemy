'''
Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estão acima da diagonal principal.
'''

import random as r 

matriz = []
vetor = []
linhas = 3
colunas = 3
soma = 0

for i in range(linhas):
    for j in range(colunas):
        num = r.randrange(0,100)
        vetor.append(num)
    matriz.append(vetor)
    vetor = []

for i in range(linhas):
    for j in range(colunas):
        print(f'{matriz[i][j]:^5}', end = ' ')
        if i < j:
            soma += matriz[i][j]
    print()

print(f'A soma dos elementos acima da diagonal principal vale {soma}.')
