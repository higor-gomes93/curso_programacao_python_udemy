'''
Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0
até N em ordem decrescente.
'''

num = int(input("Digite um numero inteiro positivo: "))

for i in range(num, -1, -1):
    print(i, end = ' ')

