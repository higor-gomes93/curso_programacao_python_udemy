'''
Faça um programa que leia um número indeterminado de idades de indivíduos (pare quando for informada)
a idade 0), e calcule a idade média nesse grupo.
'''

idade = int(input("Digite uma idade: "))
cont = 1
soma = idade

while idade > 0:
    idade = int(input("Digite uma idade: "))
    if idade > 0:
        cont += 1
        soma += idade

media = soma/cont
print(f"A idade média do grupo é {media} anos.")
