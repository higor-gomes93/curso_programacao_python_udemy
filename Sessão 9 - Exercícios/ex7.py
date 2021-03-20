'''
Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.
'''

import random

linhas = 4
colunas = 4

matriz = [[random.randint(1, 20) for j in range(colunas)] for i in range(linhas)]
print(matriz)
parcial = [len([x for x in matriz[i] if x > 10]) for i in range(linhas)]
print(sum(parcial))
