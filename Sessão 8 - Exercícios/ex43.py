'''
Faça uma função que receba um vetor de inteiros e o preencha com números aleatórios sem repetição.
'''

import random as r

def aleatorios(tamanho):
    array = []
    while len(array) < tamanho:
        num = r.randrange(1, 100)
        if num not in array:
            array.append(num)
    return array

print(aleatorios(7))
