'''
Faça uma função que receba uma matriz de 3 x 3 elementos. Calcule e retorne a soma dos elementos que estão na 
diagonal secundária.
'''

from random import randint

linhas, colunas = 3, 3

matriz = [[randint(1, 50) for j in range(colunas)] for i in range(linhas)]
[print(*matriz[i]) for i in range(linhas)]
diagsec = [matriz[i][j] for i in range(linhas) for j in range(colunas) if i+j == 2]
print(sum(diagsec))
