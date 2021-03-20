'''
Faça uma função para calcular o número neperiano usando uma série. A função deve ter como parâmetro o número de
termos que serão somados (note que, quanto maior o número, mais próxima a resposta do valor e).
'''

import math as m

def numero_neperiano(numero):
    soma = 0
    for i in range(0, numero+1):
        soma += 1/m.factorial(i)
    return soma

print(numero_neperiano(10))
