'''
Faça um programa que leia dois vetores de 10 posições e calcule outro veotr contendo, nas posições pares, os valores
do primeiro, e nas posições ímpares, os valores do segundo.
'''

vetor_a =[]
vetor_b = []
vetor_c = []
a = 0
b = 0

dicionario = {0:'primeiro', 1:'segundo', 2:'terceiro', 3:'quarto', 4:'quinto', 
5:'sexto', 6:'sétimo', 7:'oitavo', 8:'nono', 9:'décimo'}

while len(vetor_a) < 10:
    num = int(input(f'Digite o {dicionario[len(vetor_a)]} número do vetor A: '))
    vetor_a.append(num)

while len(vetor_b) < 10:
    num = int(input(f'Digite o {dicionario[len(vetor_b)]} número do vetor B: '))
    vetor_b.append(num)

for i in range(0,20):
    if i%2 == 0:
        vetor_c.append(vetor_a[a])
        a += 1
    else:
        vetor_c.append(vetor_b[b])
        b += 1

print(f'Vetor a: {vetor_a}')
print(f'Vetor b: {vetor_b}')
print(f'Vetor c: {vetor_c}')
