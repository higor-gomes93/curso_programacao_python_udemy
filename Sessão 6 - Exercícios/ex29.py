'''
Escreva um programa para calcular o valor da série para 5 termos:
S = 0 + 1/2! + 2/4! + 3/6! + ... 0.5876005842151676
'''

num  = int(input("Digite um número inteiro e positivo: "))
soma = 0
mult = 1

for i in range(1, num+1):
    for j in range(1, (2*i)+1):
        mult = mult*j
    soma = soma + i/mult
    mult = 1

print(f"A soma dos {num} primeiros termos vale {soma}.")
