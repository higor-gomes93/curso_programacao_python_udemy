'''
Faça uma função que calcule o desvio padrão de um vetor v contendo n números.
'''

import statistics

def desvpad(*args):
    soma = 0
    media = sum(args)/len(args)
    for i in args:
        soma += (i - media)**2
    desviopadrao = ((1/(len(args)-1))*soma)**0.5
    return desviopadrao

print(desvpad(2, 3, 4, 5, 6, 7))

print(statistics.stdev([2, 3, 4, 5, 6, 7]))
