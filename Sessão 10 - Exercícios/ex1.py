'''
Leia 10 números inteiros e armazene em um vetor. Em seguida, escreva os elementos que são primos e suas respectivas
posições no vetor.
'''

import random as r

lista = r.sample(range(101), 10)

def primo(x):
    cont = 0
    for i in range(1, x+1):
        if x%i == 0:
            cont += 1
    if cont <= 2:
        return x
    cont = 0

print(lista)

print({lista[x]: f'Posição {x+1}' for x in range(10) if lista[x] in map(primo, lista)})
