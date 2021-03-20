'''
Faça uma função que receba um vetor de inteiros e retorne quantos valores pares ele possui.
'''

def total_pares(*args):
    array = args
    pares = []
    for i in array:
        if i%2 == 0:
            pares.append(i)
    return len(pares)

print(total_pares(2, 3, 6, 7, 8, 9))
