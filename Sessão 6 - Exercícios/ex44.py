'''
Leia um número positivo do usuário, então, calcule e imprima a sequência de Fibonacci até o primeiro
número superior ao número lido.
'''

num = int(input("Digite um número: "))
if num <= 0:
    print(0, end = ' ')
else:
    print(0, end = ' ')
    print(1, end = ' ')

fib_1 = 0
fib_2 = 1
fib_3 = 0

while fib_3 < num:
    fib_3 = fib_1 + fib_2
    print(fib_3, end = ' ')
    fib_1 = fib_2
    fib_2 = fib_3
 