'''
Faça um programa que receba do usuário um arquivo que contenha o nome e a nota de 
diversos alunos (da seguinte forma: NOME: JOÃO NOTA: 8), um aluno por linha. Mostre 
na tela o nome e a nota do aluno que possui a maior nota.
'''

from random import uniform

raiz = 'c:/Users/Higor H/Documents/Estudos/Python'
pasta = raiz + '/Curso de Programação em Python (Udemy)/Sessão 13 - Exercícios/ex19.txt'

alunos = ['Cladio', 'Paulo', 'Jonas', 'Luis', 'Joana', 'Paula', 'Gabriela', 'Larissa',
'Camila', 'Carlos', 'Pedro', 'Tatiana']
notas = [round(uniform(0, 10.1),1) for i in range(len(alunos))]
dados = list(zip(alunos, notas))

with open(pasta, 'w', encoding='UTF-8') as arquivo:
    for i in dados:
        arquivo.write(f'NOME: {i[0].upper()} NOTA: {i[1]}\n')

with open(pasta, 'r', encoding='UTF-8') as arquivo:
    texto = arquivo.read().split('\n')
    texto.pop()
    vetor = [tuple(texto[i].split()) for i in range(len(texto))]
    notas = [float(i[3]) for i in vetor]
    for i in vetor:
        if float(i[3]) == max(notas):
            print(f'O aluno {i[1].title()} teve a maior nota, {i[3]}')
