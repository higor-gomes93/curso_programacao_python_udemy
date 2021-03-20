'''
Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número,
com exceção dele próprio.
'''

num = int(input("Insira um número positivo: "))
soma = 0

for i in range(1, num):
    if num%i == 0:
        soma = soma + i

print(f"A soma de todos os divisores de {num} é {soma}.")