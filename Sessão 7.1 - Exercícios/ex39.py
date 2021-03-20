'''
Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado Triângulo
de Pascal.
'''

tamanho = int(input('Digite o número de linhas do Triângulo de Pascal: '))
vetor = []
aux = []

for i in range(tamanho):   
    if i == 0:
        aux.append(1)
        vetor.append(aux)
        aux = []
    elif i == 1:
        aux.append(1)
        aux.append(1)
        vetor.append(aux)
        aux = []
    else:
        for j in range(i+1):
            if j == 0 or j == i:
                aux.append(1)
            else:
                num = vetor[i-1][j] + vetor[i-1][j-1]
                aux.append(num)
        vetor.append(aux)
        aux = []
    
for i in range(tamanho):
    for j in range(i+1):
        print(vetor[i][j], end = ' ')
    print()
