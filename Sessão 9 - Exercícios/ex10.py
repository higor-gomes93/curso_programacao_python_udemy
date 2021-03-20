'''
Faça uma função que receba, por parâmetro, uma matriz A[4][4] e retorna a soma dos seus elementos.
'''

from random import randint

matriz = [[randint(1,50) for j in range(4)] for i in range(4)]
[print(*matriz[i]) for i in range(4)]
soma = [matriz[i][j] for i in range(4) for j in range(4)]
print(sum(soma))
