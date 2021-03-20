'''
Faça uma função que receba como parâmetro um vetor X de 30 elementos inteiros e retorne, também por parâmetro, 
dois vetores A e B. O vetor A deve conter os elementos pares de X e o vetor B, os elementos ímpares.
'''

from random import randint

vetor = [randint(1, 101) for i in range(10)]
print(vetor)
print(f'Pares: {list(filter(lambda x:x%2==False, vetor))}\nÍmpares: {list(filter(lambda x:x%2==True, vetor))}')
