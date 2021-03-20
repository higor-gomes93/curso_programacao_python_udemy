'''
Faça uma função que receba, por parâmetro, uma matriz A[3][3] e retorna a soma dos seus elementos da sua diagonal
principal e da sua diagonal secundária.
'''

from random import randint

linhas, colunas = 3, 3

matriz = [[randint(1, 50) for j in range(colunas)] for i in range(linhas)]
[print(*matriz[i]) for i in range(linhas)]
elementos = [matriz[i][j] for i in range(linhas) for j in range(colunas) if i+j == 2 or i == j]
print(sum(elementos))
