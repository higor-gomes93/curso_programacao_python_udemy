'''
Faça um algoritmo que receba um número inteiro positivo n e calcule o somatório de 1 até n.
'''

def somatorio(numero):
    soma = 0
    for i in range(1, numero+1):
        soma += i
    return soma

print(somatorio(10))
