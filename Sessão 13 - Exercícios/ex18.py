'''
Faça um programa que leia um arquivo contendo o nome e o preço de diversos produtos
(separados por linha), e calcule o total da compra.
'''

from random import uniform

raiz = 'c:/Users/Higor H/Documents/Estudos/Python'
pasta = raiz + '/Curso de Programação em Python (Udemy)/Sessão 13 - Exercícios/ex18.txt'

produtos = ['Maçã', 'Leite Condensado', 'Papel Higiênico', 'Sabão em Pó', 'Leite',
'Detergente', 'Abobrinha', 'Sabonete', 'Pasta de Dente', 'Shampoo', 'Bolacha', 'Café']
precos = [round(uniform(1, 21),2) for i in range(len(produtos))]
tabela = zip(produtos, precos)

with open(pasta, 'w', encoding='UTF-8') as arquivo:
    for i in tabela:
        arquivo.write(f'{i[0]} - R$ {i[1]}\n')

with open(pasta, 'r', encoding='UTF-8') as arquivo:
    texto = arquivo.read().split('\n')
    texto.pop()

total = sum((float(texto[i].split()[-1]) for i in range(len(texto)))) 
print(f'Total da compra: R$ {total}')
