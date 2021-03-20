'''
Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.
'''

num = int(input("Digite um numero inteiro: "))  # Inserir o valor 50
contador = 1
soma = 0

while contador <= num:
    par = 2*contador
    soma = soma + par
    contador += 1

print(f"A soma dos {num} primeiros numeros pares eh {soma}")