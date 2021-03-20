'''
Leia 10 números inteiros e armazene em um vetor. Em seguida, escreva os elementos que são primos e suas respectivas
posições no vetor.
'''

vetor = []
cont = 0
primos = {}

while len(vetor) < 10:
    num = int(input(f'Digite o {len(vetor)+1}º número: '))
    vetor.append(num)

for i in range(0,10):
    if vetor[i] == 0:
        primos[vetor[i]] = i
    elif vetor[i] == 1:
        primos[vetor[i]] = i
    else:
        for j in range(2, vetor[i]//2 +1):
            if vetor[i]%j == 0:
                cont += 1
        if cont == 0:
            primos[vetor[i]] = i
        cont = 0

print(f'Do vetor {vetor}, temos {primos}.')
