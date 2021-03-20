'''
Gerar e imprimir uma matriz de tamanho 10 x 10, onde seus elementos são da forma:
A[i][j] = 2i + 7j - 2 se i < j;
A[i][j] = 3i² - 1 se i - j;
A[i][j] = 4i³ - 5j² se i > j.
'''

matriz = []
vetor = []
linhas = 10
colunas = 10

for i in range(linhas):
    for j in range(colunas):
        if i < j:
            num = (2*i)+(7*j) - 2
        elif i == j:
            num = (3*(i**2)) - 1
        elif i > j:
            num = (4*(i**3)) - (5*(j**2))
        vetor.append(num)
    matriz.append(vetor)
    vetor = []

for i in range(linhas):
    for j in range(colunas):
        print(f'{matriz[i][j]:^5}', end = ' ')
    print()
           