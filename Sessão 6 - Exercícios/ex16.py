'''
Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números ímpares de 0
até N em ordem decrescente.
'''

num = int(input("Digite um numero inteiro positivo impar: "))

if num%2 != 0:
    for i in range(num, 0, -2):
        print(i, end = ' ')
else:
    print("Numero invalido.")

print(0, end = ' ')

