'''
Escreva um programa que leia um inteiro não negativo n e imprima a soma dos n primeiros números
primos.
'''
total = int(input("Digite um número n não negativo: "))
check = 0
cont = 3
num = 5
soma = 6

if total == 3:
    print("A soma dos 3 primeiros primos vale 6.")
elif total == 2:
    print("A soma dos 2 primeiros primos vale 3.")
elif total == 1:
    print("A soma do primeiro primo vale 1.")

while cont < total and total > 3:
    for i in range(2, num):
        resto = num%i
        if resto == 0:
            check += 1
    if check == 0:
        cont += 1
        soma += num
    num += 1
    check = 0

print(f"A soma dos {total} primeiros primos vale {soma}.")
