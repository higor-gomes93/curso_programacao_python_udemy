'''
Crie um programa contendo as seguintes funções que recebem um vetor V de números reais como parâmetro:
- Impressão normal do vetor
- Impressão inversa
- Função que retorna a média aritmética dos elementos do vetor
'''

import random

tamanho = 10
vetor = []
i = 0

while i < tamanho:
    num = random.randrange(1, 101)
    vetor.append(num)
    i += 1

def impressao(*args):
    lista = list(args)
    print(lista)
    return

def impressao2(*args):
    print(vetor)
    return

def impressao_reversa(vetor):
    vetor.reverse()
    print(vetor)
    return

def media_vetor(vetor):
    media = sum(vetor)/len(vetor)
    return media

impressao(*vetor)
impressao2(vetor)
impressao_reversa(vetor)
print(media_vetor(vetor))
