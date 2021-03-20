'''
Em matemática, o número harmônico designado por H(n) defini-se como sendo a soma da séria harmônica:
H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n. Faça um programa que leia um valor n inteiro e positivo e 
apresente o valor de H(n).
'''

num = int(input("Digite um valor n inteiro e positivo: "))
soma = 0

for i in range(1, num+1):
    soma = soma + 1/i

print(f"A série harmônica H({num}) vale {soma}.")
