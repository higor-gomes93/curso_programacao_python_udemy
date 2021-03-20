'''
Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a união entre os 2 vetores
anteriores, ou seja, que contém apenas os números que estão em ambos os vetores. Não deve conter números repetidos.
'''

set_1 = set({})
set_2 = set({})

while len(set_1) < 10:
    num = int(input(f'Digite o {len(set_1)+1}º elemento: '))
    set_1.add(num)

while len(set_2) < 10:
    num = int(input(f'Digite o {len(set_2)+1}º elemento: '))
    set_2.add(num)

inter = set_1.union(set_2)
print(f'A união entre {set_1} e {set_2} é {inter}.')
