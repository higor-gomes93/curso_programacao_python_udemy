'''
Faça uma função não-recursiva que receba um número inteiro positivo ímpar N e retorne o fatorial duplo desse
número. O fatorial duplo é definido como o produto de todos os números naturais ímpares de 1 até algum 
número natural ímpar N.
'''

def fatorial_duplo(numero):
    if numero%2 == 0:
        return 'Número inválido'
    produto = 1
    for i in range(1, numero+1, 2):
        produto *= i
    return produto

print(fatorial_duplo(5))
