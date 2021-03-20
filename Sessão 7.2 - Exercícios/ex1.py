'''
Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.
'''

matriz = []
vetor = []
linhas = 4
colunas = 4
cont = 0

for i in range(linhas):
    for j in range(colunas):
        num = int(input(f'Digite o {j+1}º elemento da {i+1}ª linha: '))
        vetor.append(num)
    matriz.append(vetor)
    vetor = []

for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] == 10:
            cont += 1
        print(f'[{matriz[i][j]:^5}]', end = '')
    print()

if cont == 0:
    print(f'A matriz não tem nenhum elemento iguai a 10.')
elif cont == 1:
    print(f'A matriz tem {cont} elemento igual a 10.')
else:
    print(f'A matriz tem {cont} elementos iguais a 10.')
