'''
Faça um programa que leia 10 conjuntos de valores, o primeiro representando o número do aluno e o segundo representando
a sua altura em metros. Encontre o aluno mais baixo e o mais alto. Mostre o número do aluno mais baixo e do mais alto,
juntamente com suas alturas.
'''

import random as r

dicionario = {f'Aluno {i}{r.randrange(1, 11)}': float(f'1.{r.randrange(50, 99)}') for i in range(10)}
print(dicionario)

valor = [f'O {aluno} é o mais alto, com {altura}' for aluno, altura in dicionario.items()
    if altura == max(dicionario.values())]
print(valor)
