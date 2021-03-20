'''
Faça uma função não-recursiva que receba um número inteiro positivo n e retorne o fatorial exponencial desse número. Um 
fatorial exponencial é um inteiro positivo n elevado à potência (n-1), que por sua vez é elevado à potência (n-2), e 
assim em diante.
'''

def fat_exp(numero):
    produto = numero
    for i in range(1, numero):
        produto = produto**(numero-i)
    return produto

print(fat_exp(3))
