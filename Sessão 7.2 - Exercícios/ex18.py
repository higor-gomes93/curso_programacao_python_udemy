'''
Faça um programa que permita ao usuário entrar com uma matriz de 3 x 3 números inteiros. Em seguida, gere
um array unidimensional pela soma dos números de de cada coluna da matriz e mostrar na tela esse array.  
'''

import random as r 

matriz = []
vetor = []
array = []
linhas = 3
colunas = 3

print()

for i in range(linhas):
    for j in range(colunas):
        num = r.randrange(-100, 101)
        vetor.append(num)
    matriz.append(vetor)
    vetor = []

for i in range(linhas):
    for j in range(colunas):
        aux = matriz[j][i]
        vetor.append(aux)
    soma = sum(vetor)
    array.append(soma)
    vetor = []
    soma = []

for i in range(linhas):
    for j in range(colunas):
        print(f'[{matriz[i][j]:^5}]', end = ' ')
    print()

print('-'*23)

for i in range(3):
    print(f'[{array[i]:^5}]', end = ' ')
print()
