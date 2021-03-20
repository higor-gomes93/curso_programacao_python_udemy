'''
Leia um vetor de 10 posições e atribua valor 0 para todos os elementos que possuírem valores negativos.
'''

import random as r

vetor = r.sample(range(-10, 11), 10)
print(vetor)
res = [x if x > 0 else 0 for x in vetor]
print(res)
