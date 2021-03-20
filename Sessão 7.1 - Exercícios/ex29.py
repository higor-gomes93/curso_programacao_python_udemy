'''
Faça um programa que receba 6 número inteiros e mostre:
- Os números digitados;
- A soma dos números pares digitados;
- Os números ímpares digitados;
- A quantidade de números ímpares digitados.
'''

vetor_v = []
vetor_v1 = []
vetor_v2 = []

while len(vetor_v) < 6:
    num = int(input(f'Digite o {len(vetor_v)+1}º número: '))
    vetor_v.append(num)

for i in range(0,6):
    num = vetor_v[i]
    if num%2 != 0:
        vetor_v1.append(num)
    elif num%2 == 0:
        vetor_v2.append(num)

print(f'Os números digitados: {vetor_v}.')
print(f'A soma dos números pares digitados: {sum(vetor_v2)}.')
print(f'Os números ímpares digitados: {vetor_v1}.')
print(f'A quantidade de números ímpares digitados: {len(vetor_v1)}.')
