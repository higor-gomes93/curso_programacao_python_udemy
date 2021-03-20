'''
Faça um função chamada 'simplifica' que recebe como parâmetro o numerador e o denominador de uma fração. Esta
função deve simplificar a fração recebida dividindo o numerador e o denominador pelo maior fator possível. 
'''

def simplifica(numerador, denominador):
    tupla = (numerador, denominador)
    limite = max(tupla)
    for i in range(1, limite+1):
        if numerador%i == 0 and denominador%i == 0:
            fator = i
    return f'A fração {numerador}/{denominador} equivale a {int(numerador/fator)}/{int(denominador/fator)}.'

print(simplifica(52, 132))
