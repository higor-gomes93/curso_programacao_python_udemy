'''
Faça uma função não-recursiva que receba um número inteiro positivo n e retorne o fatorial quádruplo desse número.
O fatorial quádruplo de um número n é dado por: (2n)!/n!
'''

def fatorial_quadruplo(numero):
    numerador = 1
    denominador = 1
    for i in range(1, 2*numero +1):
        numerador *= i
    for i in range(1, numero+1):
        denominador *= i
    return numerador/denominador

print(fatorial_quadruplo(3))
