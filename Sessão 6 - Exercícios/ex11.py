'''
Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0
até N em ordem crescente.
'''

num = int(input("Digite um numero inteiro positivo: "))

for i in range(0, num+1):
    print(i, end = ' ')

