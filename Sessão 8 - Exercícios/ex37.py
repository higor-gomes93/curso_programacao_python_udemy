'''
Faça uma função não-recursiva que receba um número inteiro positivo n e retorne o hiperfatorial desse número. O 
hiperfatorial de um número n, escrito H(n), é definido por: H(n) = 1¹ * 2² * 3³ * ... * n^n.
'''

def hiperfatorial(numero):
    produto = 1
    for i in range(1, numero+1):
        produto *= i**i
    return produto

print(hiperfatorial(3))
