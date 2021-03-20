'''
Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares.
'''

num = int(input("Digite um numero inteiro: "))
contador = 0

while contador < num:
    impar = 2*contador + 1
    print(impar)
    contador += 1

