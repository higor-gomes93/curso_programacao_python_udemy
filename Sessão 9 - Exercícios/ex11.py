'''
Leia um número positivo do usuário, então, calcule e imprima a sequência de Fibonacci até o primeiro
número superior ao número lido.
'''

lista = [0, 1]
num = int(input('Digite um número inteiro: '))
[lista.append(lista[i-1]+lista[i-2]) for i in range(2, num) if lista[-1] < num]
print(lista)
