'''
Escreva uma função que gere um triângulo de altura e lados n e base 2*n-1.
'''

def triangulo(numero):
    for i in range(1, numero+1):
        elemento = '*'*(2*i -1)
        print(f'{elemento:^{numero*2}}')
    return

triangulo(6)
