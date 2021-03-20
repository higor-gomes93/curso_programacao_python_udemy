'''
Escreva um programa que leia números inteiros no intervalo [0,50] e os armazene em um vetor com 10 posições. Preencha
um segundo vetor apenas com os números ímpares do primeiro vetor. Imprima os dois vetores, 2 elementos por linha.
'''

vetor = []
impares = []
intervalo_string = '[0, 50]'
intervalo = range(0,51)

while len(vetor) < 10:
    num = int(input(f'Digite um número inteiro no intervalo {intervalo_string}: '))
    if num in intervalo:
        vetor.append(num)
    else:
        print(f'O número {num} está fora do intervalo {intervalo_string}')

for elemento in vetor:
    if elemento%2 != 0:
        impares.append(elemento)

indice_1 = 0
while indice_1 < len(vetor):
    print(vetor[indice_1], end=' ')
    indice_1 += 1
    if indice_1 < len(vetor):
        print(vetor[indice_1])
    indice_1 += 1

print('-' * 80)

indice_2 = 0
while indice_2 < len(impares):
    print(impares[indice_2], end=' ')
    indice_2 += 1
    if indice_2 < len(impares):
        print(impares[indice_2])
    indice_2 += 1
