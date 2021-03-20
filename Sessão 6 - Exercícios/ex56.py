'''
Faça um programa que calcule a soma de todos os números primos abaixo de dois milhões.
'''
total = int(input("Digite o valor limite para o número primo: "))  # Inserir 2.000.000
check = 0
cont = 0
num = 5
soma = 6

if total == 3:
    print("A soma dos 3 primeiros primos vale 3.")
elif total == 2:
    print("A soma dos 2 primeiros primos vale 2.")
elif total == 1:
    print("A soma do primeiro primo vale 1.")

while num < total and total > 3:
    for i in range(2, num):
        resto = num%i
        if resto == 0:
            check += 1
    if check == 0:
        soma += num
    num += 1
    check = 0

print(f"A soma dos primos abaixo de {total} vale {soma}")
