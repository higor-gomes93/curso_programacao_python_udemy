'''
Leia uma matriz 5 x 5. Leia também um valor X. O programa deverá fazer uma busca desse valor na matriz e, ao final,
escrever a localização (linha e coluna) ou uma mensagem de "não encontrado".
'''

import random as r 

matriz = []
vetor = []
linhas = 5
colunas = 5
check = 0

for i in range(linhas):
    for j in range(colunas):
        num = r.randrange(0, 15)
        vetor.append(num)
    matriz.append(vetor)
    vetor = []

x = int(input('Digite um número x: '))

for i in range(linhas):
    for j in range(colunas):
        print(f'{matriz[i][j]:^3}', end = ' ')
    print()

for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] == x:
            print(f'O número está na linha {i+1} e coluna {j+1}.')
            check += 1

if check == 0:
    print(f'O número {x} não está presente na matriz.')
