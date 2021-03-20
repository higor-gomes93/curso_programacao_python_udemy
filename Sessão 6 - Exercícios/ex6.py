'''
Faça um programa que leia 10 inteiros e imprima sua média.
'''
soma = 0
total = 0

for i in range(1, 11):
    num = int(input(f"Insira o numero {i}: "))
    soma = soma + num
    total = i
media = soma/total
print(f"A media dos numeros eh {media}!")

