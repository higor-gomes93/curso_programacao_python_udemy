'''
Faça um programa que conte quantos números primos existem entre a e b, onde a e b são números
informados pelo usuário.
'''

num_a = int(input("Digite o limite inferior: "))
num_b = int(input("Digite o limite superior: "))
cont = 0
total = 0

for i in range(num_a, num_b+1):
    if i == 1:
        total += 1
    if i == 2:
        total += 1
    if i > 2:
        for j in range(2, i):
            resto = i%j
            if resto == 0:
                cont += 1
        if cont == 0:
            total += 1
    cont = 0

print(f"Entre {num_a} e {num_b} existem {total} primos.")
