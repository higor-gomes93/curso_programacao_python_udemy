'''
Faça um programa que calcule e escreva o valor de S.
S = 1/1 + 3/2 + 5/3 + 7/4 ... 99/50
'''

from fractions import Fraction

limite = int(input("Insira a quantidade de termos: "))  # Inserir o valor 50
soma = 0

for i in range(1, limite):
    soma = soma + (2*1 - 1)/i
    # valor = Fraction((2*i - 1), i)  -> Usando a biblioteca Fraction para checar as frações
    # print(valor)

print(f"O valor de S é {soma}.")
