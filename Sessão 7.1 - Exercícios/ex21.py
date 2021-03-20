'''
Faça um programa que receba do usuário dois vetores, A e B, com 10 números inteiros cada. Crie um novo vetor
denominado C calculando C = A - B. Mostre na tela os dados do vetor C.
'''

vetor_a = []
vetor_b = []
vetor_c = []
i = 0
dicionario = {0:'primeiro', 1:'segundo', 2:'terceiro', 3:'quarto', 4:'quinto', 
5:'sexto', 6:'sétimo', 7:'oitavo', 8:'nono', 9:'décimo'}

while len(vetor_a) < 10:
    num = int(input(f'Digite o {dicionario[len(vetor_a)]} número do vetor A: '))
    vetor_a.append(num)

while len(vetor_b) < 10:
    num = int(input(f'Digite o {dicionario[len(vetor_b)]} número do vetor B: '))
    vetor_b.append(num)

while i < 10:
    num = vetor_a[i] - vetor_b[i]
    vetor_c.append(num)
    i += 1

print(f'A operação {vetor_a} - {vetor_b} vale {vetor_c}.')
