'''
Leia uma matriz 5 x 10 que se refere a respostas de 10 questões de múltipla escolha, referentes a 5 alunos. Leia
também um vetor de 10 posições contendo o gabarito de respostas que podem ser a, b, c ou d. Seu programa deverá
comparar as respostas de cada candidato com o gabarito e emitir um vetor denominado resultado, contendo a pontuação
correspondente de cada aluno.
'''

import random as r 

matriz = []
vetor = []
gabarito = []
resultado = []
respostas = ['a', 'b', 'c', 'd']
linhas = 5
colunas = 10
soma = 0

print('-'*19)

for i in range(linhas):
    for j in range(colunas):
        resp = r.choice(respostas)
        vetor.append(resp)
    matriz.append(vetor)
    vetor = []

for i in range(colunas):
    result = r.choice(respostas)
    resultado.append(result)
    print(resultado[i], end = ' ')
print()
print('-'*19)

for i in range(linhas):
    for j in range(colunas):
        print(matriz[i][j], end = ' ')
    print()
print('-'*19)

for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] == resultado[j]:
            soma += 1
    gabarito.append(soma)
    soma = 0
    print(gabarito[i], end = ' ')
