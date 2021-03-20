'''
Faça um programa que recebe como entrada o nome de um arquivo de entrada e o nome de um arquivo
de saída. O arquivo de entrada contém o nome de um aluno e três inteiros que indicam suas notas.
O programa deverá ler o arquivo de entrada e gerar um arquivo de saída onde aparece o nome do
aluno e as suas notas em ordem crescente.
'''

from random import choice, uniform

raiz = 'c:/Users/Higor H/Documents/Estudos/Python'
pasta1 = raiz + '/Curso de Programação em Python (Udemy)/Sessão 13 - Exercícios/ex22_1.txt'
pasta2 = raiz + '/Curso de Programação em Python (Udemy)/Sessão 13 - Exercícios/ex22_2.txt'

with open(pasta1, 'w', encoding='UTF-8') as arquivo:
    nome = input('Digite o nome do aluno: ')
    notas = []
    for i in range(3):
        nota = input(f'Digite a {i+1}ª nota: ')
        notas.append(nota)
    arquivo.write(f'{nome} - {notas[0]} {notas[1]} {notas[2]}')

with open(pasta1, 'r', encoding='UTF-8') as arquivo:
    dados = arquivo.read().split()

notas = (int(dados[-1]), int(dados[-2]), int(dados[-3]))
aluno = ''
for i in dados:
    if i != '-':
        aluno += f'{i} '
    else:
        break

notas_final = sorted(notas)

with open(pasta2, 'w', encoding='UTF-8') as arquivo:
    arquivo.write(f'Aluno: {aluno.strip()} - Notas: {notas_final[0]} {notas_final[1]} {notas_final[2]}')
