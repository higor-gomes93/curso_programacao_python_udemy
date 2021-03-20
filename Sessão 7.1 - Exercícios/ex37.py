'''
Considere um vetor A com 11 elementos onde A1 < A2 < ... < A6 > A7 > A8 > ... > A11, ou seja, está ordenado em
ordem crescente até o sexto elemento, e a partir desse elemento está ordenado em ordem decrescente. Dado o vetor
da questão anterior, proponha um algoritmo para ordenar os elementos.
'''

import random as r

vetor = []
vetor_1 = []
vetor_2 = []

while len(vetor) < 11:
    num = r.randrange(100)
    vetor.append(num)

print(vetor)

for i in range(0, 6):
    num = vetor[i]
    vetor_1.append(num)

vetor_1.sort()
print(vetor_1)

for i in range(6, 11):
    num = vetor[i]
    vetor_2.append(num)

vetor_2.sort()
vetor_2.reverse()
print(vetor_2)

vetor_1.extend(vetor_2)
print(vetor_1)
