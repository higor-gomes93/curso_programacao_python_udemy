'''
Faça um programa que leia um vetor de 15 posições e o compacte, ou seja, elimine as posições com valor zero. Para
isso, todos os elementos à frente do valor zero devem ser movidos uma posição para trás no vetor.
'''

vetor = []
i = 0
j = 15

while len(vetor) < j:
    num = int(input(f'Digite o {len(vetor)+1}º número: '))
    vetor.append(num)

print(f'Vetor: {vetor}.')

while i < j:
    if vetor[i] == 0:
        vetor.pop(i)
        j -= 1
    i += 1

print(f'Vetor compactado: {vetor}.')
