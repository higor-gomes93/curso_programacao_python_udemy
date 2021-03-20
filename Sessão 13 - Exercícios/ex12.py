'''
Abra um arquivo de texto, calcule e escreva o número de caracteres, o número de linhas
e o número de palavras neste arquivo. Escreva também quantas vezes cada letra ocorre
no arquivo (ignorando letras com acento).
'''

from collections import Counter

raiz = 'c:/Users/Higor H/Documents/Estudos/Python'
pasta = raiz + '/Curso de Programação em Python (Udemy)/Sessão 13 - Exercícios/arquivo.txt'
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

with open(pasta, 'r', encoding='UTF-8') as arquivo:
    caracteres = arquivo.read()

with open(pasta, 'r', encoding='UTF-8') as arquivo:
    linhas = arquivo.readlines()

with open(pasta, 'r', encoding='UTF-8') as arquivo:
    palavras = arquivo.read().split()

contador = Counter(filter(lambda x: x in alfabeto, caracteres.lower()))

print(f'Total de caracteres: {len(caracteres)}.')
print(f'Total de linhas: {len(linhas)}.')
print(f'Total de palavras: {len(palavras)}.')
print(f'Ocorrência de cada letra: {contador}.')
