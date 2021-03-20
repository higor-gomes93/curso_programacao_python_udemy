'''
Faça uma função que receba como parâmetro um vetor X de 30 elementos inteiros e retorne, também por parâmetro, 
dois vetores A e B. O vetor A deve conter os elementos pares de X e o vetor B, os elementos ímpares.
'''

def pares_impares(*args):
    A = []
    B = []
    for i in args:
        if i%2 == 0:
            A.append(i)
        elif i%2 != 0:
            B.append(i)
    return f'Pares: {A}\nÍmpares: {B}'

print(pares_impares(2, 4, 6, 7, 12, 75))
