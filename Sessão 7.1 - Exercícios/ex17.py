'''
Leia um vetor de 10 posições e atribua valor 0 para todos os elementos que possuírem valores negativos.
'''

vetor = []

while len(vetor) < 10:
    num = int(input('Digite um número: '))
    vetor.append(num)

print(vetor)

for i in range(0,10):
    if vetor[i] < 0:
        vetor[i] = 0

print(vetor)
