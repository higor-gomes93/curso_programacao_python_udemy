'''
Faça um programa que calcule o desvio padrão de um vetor v contendo n = 10 números, onde m é a média do vetor.
'''

vetor = []
soma = []
i = 0

while len(vetor) < 10:
    num = float(input(f'Digite o {len(vetor)+1}º número: '))
    vetor.append(num)

while i < 10:
    fator = (vetor[i] - (sum(vetor)/10))**(2)
    soma.append(fator)
    i += 1

desvpad = round(((1/9)*sum(soma))**(0.5),3)
print(f'O desvio padrão do vetor {vetor} é {desvpad}.')
