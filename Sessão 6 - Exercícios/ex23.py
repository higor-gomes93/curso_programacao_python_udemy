'''
Faça um algoritmo que leia um número positivo e imprima seus divisores.
'''

num = int(input("Insira um número positivo: "))

for i in range(1, num+1):
    if num%i == 0:
        print(f"{i} é um divisor de {num}.")
