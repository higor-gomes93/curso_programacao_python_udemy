'''
Faça um algoritmo que receba um número inteiro positivo n e calcule o seu fatorial n!.
'''

def fatorial(numero):
    produto = 1
    for i in range(1, numero+1):
        produto = i*produto
    return produto

print(fatorial(5))
