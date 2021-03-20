'''
Faça uma função que receba uma matriz de 3 x 3 elementos. Calcule e retorne a soma dos elementos que estão na 
diagonal principal.
'''

from random import randint

matriz = [[f'{randint(1, 50):^3}' for j in range(3)] for i in range(3)]
[print(*matriz[i]) for i in range(3)]
soma = [int(matriz[i][j]) for j in range(3) for i in range(3) if j==i]
print(sum(soma))
