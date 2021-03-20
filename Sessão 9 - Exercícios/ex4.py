'''
Faça um programa que leia um vetor de 10 números. Leia um número x. Conte os múltiplos de um número inteiro x num
vetor e mostre-os na tela.
'''

import random as r 

vetor = r.sample(range(101), 10)
num = int(input('Digite um número x: '))
print(vetor)
mult = [x for x in vetor if not x%num]
print(mult)
