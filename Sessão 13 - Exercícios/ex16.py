'''
Faça um programa que recebe um vetor de 10 números, converta cada um desses números para
binário e grave a sequência de 0s e 1s em um arquivo texto. Cada número deve ser gravado
em uma linha.
'''

from random import randint

raiz = 'c:/Users/Higor H/Documents/Estudos/Python'
pasta = raiz + '/Curso de Programação em Python (Udemy)/Sessão 13 - Exercícios/ex16.txt'

vetor = [randint(1, 101) for i in range(10)]

with open(pasta, 'w', encoding='UTF-8') as arquivo:
    for i in vetor:
        arquivo.write(f'{str(bin(i))[2:]}\n')
