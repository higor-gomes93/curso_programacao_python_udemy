'''
Faça uma função que receba um número N e retorne a soma dos algarismos de N!.
'''

from functools import reduce

fatorial = reduce(lambda x, y: x*y, range(1, int(input('Digite um número inteiro: '))+ 1))
soma = [int(i) for i in str(fatorial)]
print(sum(soma))
