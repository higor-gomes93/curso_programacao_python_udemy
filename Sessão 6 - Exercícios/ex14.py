'''
Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0
até N em ordem decrescente.
'''

num = int(input("Digite um numero inteiro positivo par: "))

if num%2 == 0:
    for i in range(num, -1, -2):
        print(i, end = ' ')
else:
    print("Numero invalido.")

