'''
Faça um programa que some os números primos existem entre a e b, onde a e b são números
informados pelo usuário.
'''

num_a = int(input("Digite o limite inferior: "))
num_b = int(input("Digite o limite superior: "))
cont = 0
soma = 0

for i in range(num_a, num_b+1):
    if i == 1:
        soma += 1
    if i == 2:
        soma += 3
    if i > 2:
        for j in range(2, i):
            resto = i%j
            if resto == 0:
                cont += 1
        if cont == 0:
            soma += i
    cont = 0

print(f"A soma dos primos entre {num_a} e {num_b} vale {soma}.")
