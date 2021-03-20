'''
Faça um programa que some os termos de valor par da sequência de Fibonacci, cujos valores não
ultrapassem quatro milhões.
'''

num = 4000000
soma = 0
fib_1 = 0
fib_2 = 1
fib_3 = 0

while True:
    fib_3 = fib_1 + fib_2
    if fib_3%2 == 0 and fib_3 < num:
        soma = soma + fib_3
    elif fib_3 >= num:
        break
    fib_1 = fib_2
    fib_2 = fib_3

print(soma)
