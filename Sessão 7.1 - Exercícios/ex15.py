'''
Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando elementos repetidos.
'''

vetor = []

while len(vetor) < 20:
    num = int(input('Digite um número inteiro: '))
    vetor.append(num)

vetor_filtro = set(vetor)
vetor_final = list(vetor_filtro)

print(vetor)
print(vetor_final)