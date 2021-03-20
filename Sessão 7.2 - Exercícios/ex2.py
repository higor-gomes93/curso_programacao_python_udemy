'''
Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais elementos. Escreva ao final a
matriz obtida.
'''

matriz = []
vetor = []
linhas = 5
colunas = 5

for i in range(linhas):
    for j in range(colunas):
        if i == j:
            vetor.append(1)
        else:
            vetor.append(0)
    matriz.append(vetor)
    vetor = []

for i in range(linhas):
    for j in range(colunas):
        print(f'{matriz[i][j]}', end = ' ')
    print()
