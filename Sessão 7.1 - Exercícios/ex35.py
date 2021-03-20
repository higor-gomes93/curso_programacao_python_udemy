'''
Faça um programa que leia dois números a e b (positivos menores que 10000) e:
- Crie um vetor onde cada posição é um algarismo do número. A primeira posição é o algarismo menos significativo
- Crie um vetor que seja a soma de a e b, mas faça-o usando apenas os vetores construídos anteriormente
Dica: some as posições correspondentes. Se a soma ultrapassar 10, subtraia 10 do resultado e some 1 à próxima
posição.
'''

num_a = int(input('Digite o número a: '))
num_b = int(input('Digite o número b: '))
num_a = str(num_a)
num_b = str(num_b)
vetor_a = []
vetor_b = []
vetor_soma = []
cont_a = 0
cont_b = 0
cont_soma = 0
fator = 0

# Quebrando a
for i in num_a:
    num = int(i)
    vetor_a.append(num)

while len(vetor_a) < 5:
    vetor_a.insert(cont_a, 0)
    cont_a += 1

# Quebrando b
for i in num_b:
    num = int(i)
    vetor_b.append(num)

while len(vetor_b) < 5:
    vetor_b.insert(cont_b, 0)
    cont_b += 1

# Somando a e b
for i in range(4,-1,-1):
    if vetor_a[i] + vetor_b[i] + fator < 10:
        num = vetor_a[i] + vetor_b[i] + fator
        vetor_soma.append(num)
        fator = 0
    elif vetor_a[i] + vetor_b[i] + fator > 10:
        num = vetor_a[i] + vetor_b[i] + fator - 10
        vetor_soma.append(num)
        fator = 1

while len(vetor_soma) < 5:
    vetor_soma.insert(cont_soma, 0)
    cont_soma += 1

num_a = int(num_a)
num_b = int(num_b)
vetor_soma.reverse()
print(f'A soma de {num_a} com {num_b} vale {vetor_soma}.')
