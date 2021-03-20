'''
Faça um programa que leia um valor N inteiro e positivo, calcule e mostre o valor de E, conforme a
fórmula a seguir: E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
'''

# Primeira maneira
import math as m

num = int(input("Insira um número inteiro e positivo: "))
soma = 1

for i in range(1, num+1):
    soma  = soma + 1/m.factorial(i)

print(f"Para o número {num}, o valor de E é {soma}.")


# Segunda maneira

num = int(input("Insira um número inteiro e positivo: "))
soma = 1
mult = 1

for i in range(1, num+1):
    mult = mult*i
    soma = soma + 1/mult

print(f"Para o número {num}, o valor de E é {soma}.")
