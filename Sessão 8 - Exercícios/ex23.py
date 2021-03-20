'''
Escreva uma função que gere um triângulo lateral de altura 2*n-1 e largura n.
'''

def triangulo(numero):
    for i in range(1, numero+1):
        print('*'*i)
    for i in range(numero-1, 0, -1):
        print('*'*i)
    return

triangulo(4)
