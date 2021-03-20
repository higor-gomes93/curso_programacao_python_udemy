'''
Leia uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e coluna) do maior valor
'''

matriz = []
vetor = []
linhas = 4
colunas = 4
maximo = 0

for i in range(linhas):
    for j in range(colunas):
        num = int(input(f'Digite o {j+1}º elemento da {i+1}ª linha: '))
        vetor.append(num)
    matriz.append(vetor)
    vetor = []

for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] >= maximo:
            maximo = matriz[i][j]
            max_linha = i+1
            max_coluna = j+1
        print(f'{matriz[i][j]:^5}', end = ' ')
    print()

print(f'O maior elemento, {maximo}, está localizado na linha {max_linha} e na coluna {max_coluna}.')
