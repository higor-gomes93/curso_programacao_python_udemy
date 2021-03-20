'''
Faça um programa que preencha uma matriz 4 x 4 com o produto do valor da linha e da coluna de cada elemento.
Em seguida, imprima na tela a matriz.
'''

matriz = []
vetor = []
linhas = 4
colunas = 4

for i in range(linhas):
    for j in range(colunas):
        num = (i+1)*(j+1)
        vetor.append(num)
    matriz.append(vetor)
    vetor = []

for i in range(linhas):
    for j in range(colunas):
        print(f'{matriz[i][j]:^5}', end = ' ')
    print()
