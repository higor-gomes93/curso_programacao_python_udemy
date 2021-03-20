'''
Leia um vetor com 10 números reais, ordene os elementos deste vetor, e no final escreva os elementos do vetor ordenado.
'''

vetor = []

while len(vetor) < 10:
    num = int(input(f'Digite o {len(vetor)+1}º número do vetor: '))
    vetor.append(num)

vetor.sort()

for i in range(0, 10):
    print(vetor[i], end = ' ')
