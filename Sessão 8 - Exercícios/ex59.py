'''
Faça uma função que recebe, por parâmetro, 2 vetores de 10 elementos inteiros e que calcule e retorne, também por
parâmetro, o vetor união dos dois primeiros.
'''

import random as r

tamanho = 10
vetor_a = []
vetor_b = []


for i in range(tamanho):
    num_1 = r.randrange(1, tamanho**2 +1)
    vetor_a.append(num_1)
    num_2 = r.randrange(1, tamanho**2 +1)
    vetor_b.append(num_2)

print(vetor_a)
print(vetor_b)

def uniao_vetores(A, B):
    A.extend(B)
    return A

print(uniao_vetores(vetor_a, vetor_b))
