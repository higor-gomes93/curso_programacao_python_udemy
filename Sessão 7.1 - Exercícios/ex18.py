'''
Faça um programa que leia um vetor de 10 números. Leia um número x. Conte os múltiplos de um número inteiro x num
vetor e mostre-os na tela.
'''

vetor = []
multiplos = []
dicionario = {0:'primeiro', 1:'segundo', 2:'terceiro', 3:'quarto', 4:'quinto', 
5:'sexto', 6:'sétimo', 7:'oitavo', 8:'nono', 9:'décimo'}

while len(vetor) < 10:
    num = int(input(f'Digite o {dicionario[len(vetor)]} número: '))
    vetor.append(num)

num_x = int(input('Digite um número x: '))

for elemento in vetor:
    if elemento%num_x == 0:
        multiplos.append(elemento)

if len(multiplos) == 0:
    print(f'Dentro do vetor {vetor}, não há múltiplos de {num_x}.')
else:
    print(f'Dentro do vetor {vetor}, os múltiplos de {num_x} são {multiplos}.')
