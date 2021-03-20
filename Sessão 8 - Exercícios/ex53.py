'''
Escreva uma função que verifica se uma matriz quadrada de ordem N é a matriz identidade.
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
    cont_1 = 0
    cont_2 = 0
    for i in range(ordem):
        for j in range(ordem):
            if i != j:
                if args[i][j] != 0:
                    cont_1 += 1
            if i == j:
                if args[i][j] != 1:
                    cont_2 += 1
    if cont_1 == 0 and cont_2 == 0:
        print('É uma matriz identidade.')
    else:
        print('Não é uma matriz identidade.')
    return

teste = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

chama_matriz(*matriz)
chama_matriz(*teste)
