'''
Faça um programa para gerar automaticamente números entre 0 e 99 de uma cartela de bingo. Sabendo que cada cartela
deverá conter 5 linhas de 5 números, gere estes dados de modo a não ter números repetidos dentro das cartelas. O
programa deve exibir a cartela gerada.
'''

import random as r

matriz = []
vetor = []
linhas = 5
colunas = 5
lista = list(range(1,100))

for i in range(linhas):
    for j in range(colunas):
        num = r.choice(lista)
        vetor.append(num)
        lista.remove(num)
    matriz.append(vetor)
    vetor = []

for i in range(linhas):
    for j in range(colunas):
        print(f'{matriz[i][j]:^3}', end = ' ')
    print()
