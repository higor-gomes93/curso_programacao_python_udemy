'''
Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números ímpares de 0
até N em ordem crescente.
'''

num = int(input("Digite um numero inteiro positivo impar: "))

if num%2 != 0:
    print(0, end = ' ')
    for i in range(1, num+1, 2):
        print(i, end = ' ')
else:
    print("Numero invalido.")

