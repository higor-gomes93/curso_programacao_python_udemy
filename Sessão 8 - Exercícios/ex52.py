'''
Escreva uma função que receba uma matriz quadrada de ordem N e calcule a sua transposta.
'''

import random as r

matriz = []
vetor = []
ordem = 3

for i in range(ordem):
    for j in range(ordem):
        num = r.randrange(1, ordem**2 +1)
        vetor.append(num)
    matriz.append(vetor)
    vetor = []

for i in range(ordem):
    for j in range(ordem):
        print(f'{matriz[i][j]:^2}', end = ' ')
    print()

print()

def chama_matriz(*args):
    for i in range(ordem):
        for j in range(ordem):
            print(f'{args[j][i]:^2}', end = ' ')
        print()
    return

chama_matriz(*matriz)
