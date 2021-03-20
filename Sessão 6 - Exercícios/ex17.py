'''
Faça um programa que leia um número inteiro positivo N e calcule a soma dos N primeiros números
naturais.
'''

num = int(input("Digite um numero inteiro positivo: "))
soma = 0

if num >= 0:
    for i in range(0, num+1, 1):
        soma = soma + i
else:
    print("Numero invalido.")

print(f"A soma dos {num} primeiros numeros naturais eh {soma}")

