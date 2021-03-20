'''
Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número,
com exceção dele próprio.
'''

num = int(input("Insira um número positivo: "))

lista = [div for div in range(1, num) if num%div == 0]

print(sum(lista))
