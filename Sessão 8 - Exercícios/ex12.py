'''
Escreva um programa que receba um número inteiro maior do que zero e retorne a soma de todos os seus algarismos.
Se o número lido não for maior do que zero, o programa terminará com a mensagem 'Número inválido'.
'''

def soma_alg(num):
    convert = str(num)
    i = 0
    array = []
    if num < 0:
        return 'Número inválido.'
    while i < len(convert):
        number = int(convert[i])
        array.append(number)
        i += 1
    return sum(array)

print(soma_alg(354))
print(soma_alg(5234))
print(soma_alg(23))
print(soma_alg(0))
print(soma_alg(-25))
