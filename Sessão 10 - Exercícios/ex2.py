'''
Faça um código que retorne o maior fator primo de um número.
'''

numero = int(input('Digite um número: '))

res = [[i/j for j in range(1, i+1) if i%j == 0] for i in range(1, numero+1)]
primosfinal = map(lambda x: int(x[0]), filter(lambda x: len(x) <= 2, res))

print(max(primosfinal))
