'''
Peça ao usuário para digitar dez valores numéricos e ordene por ordem crescente esses valores, guardando-os
num vetor. Ordene o valor assim que ele for digitado. Mostre na tela os valores em ordem.
'''

vetor = []

while len(vetor) < 10:
    num = int(input(f'Digite o {len(vetor)+1}º número do vetor: '))
    vetor.append(num)
    vetor.sort()

print(f'O vetor ordenado é {vetor}.')
