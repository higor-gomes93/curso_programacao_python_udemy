'''
Faça um programa que receba um número inteiro maior do que 1, e verifique se o número fornecido
é primo ou não.
'''

num = int(input("Digite um número inteiro maior que 1: "))
check = 0

while num > 1:
    for i in range(2, num):
        resto = num%i
        if resto == 0:
            check += 1
    if check == 0:
        print(f"O número {num} é primo.")
    else:
        print(f"O número {num} não é primo.")
    check = 0        
    num = int(input("Digite um número inteiro maior que 1: "))

print("Até mais!")
