'''
Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.
'''

num = int(input("Digite um numero: "))

if num == 1:
    print("O numero eh impar.")
elif num%2 == 0:
    print("O numero eh par.")
else:
    print("O numero eh impar.")