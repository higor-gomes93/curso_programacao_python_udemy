'''
Leia 10 números inteiros e armaneze em um vetor v. Crie dois vetores v1 e v2. Copie os valores ímpares de v para v1, 
e os valores pares de v para v2. Note que cada um dos vetores v1 e v2 têm no máximo 10 elementos, mas nem todos os
elementos são utilizados. No final escreva os elementos utilizados de v1 e v2.
'''

vetor_v = []
vetor_v1 = []
vetor_v2 = []

while len(vetor_v) < 10:
    num = int(input(f'Digite o {len(vetor_v)+1}º número: '))
    vetor_v.append(num)

for i in range(0,10):
    num = vetor_v[i]
    if num%2 != 0:
        vetor_v1.append(num)
    elif num%2 == 0:
        vetor_v2.append(num)

tamanho1 = []
tamanho2 = []

for i in range(0,len(vetor_v1)):
    tamanho1.append(i)

for i in range(0,len(vetor_v2)):
    tamanho2.append(i)

print(f'Foram utilizados os elementos {tamanho1} no vetor v1 e os elementos {tamanho2} no vetor v2.')
  