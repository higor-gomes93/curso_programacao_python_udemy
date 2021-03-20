'''
Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva
na tela.
'''

# Forma 1
valores = []

while len(valores) < 10:
    num = float(input('Digite um número: '))
    valores.append(num)

valores_set = set(valores)
valores_unicos = list(valores_set)

for i in valores_unicos:
    valores.remove(i)

print(valores)


# Forma 2
from collections import Counter

valores = []

while len(valores) < 10:
    num = float(input('Digite um número: '))
    valores.append(num)

total = Counter(valores)

for indice in total:
    if total[indice] > 1:
        print(f"O número {indice} ocorreu {total[indice]} vezes.")
