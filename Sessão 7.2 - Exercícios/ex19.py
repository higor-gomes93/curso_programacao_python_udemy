'''
Faça um programa que leia uma matriz de 5 linhas e 4 colunas contendo as seguintes informações sobre os alunos
de uma disciplina, sendo todas as informações do tipo inteiro:
- primeira coluna: número de matrícula
- segunda coluna: média das provas
- média dos trabalhos
- quarta coluna: nota final
Elabore um programa que:
a) Leia as três primeiras informações de cada aluno
b) Calcule a nota final como sendo a soma da média das provas e da média dos trabalhos
c) Imprima a mtrícula do aluno que obteve a maior nota final (assuma que só existe uma maior nota)
d) Imprima a média aritmética das notas finais
'''

import random as r  

matriz = []
vetor = []
linhas = 5
colunas = 4

print()

for i in range(linhas):
    for j in range(colunas):
        if j == 0:
            num = r.randrange(140000, 150000)
            vetor.append(num)
        elif j == 1 or j == 2:
            num = r.randrange(0, 11)
            vetor.append(num)
        elif j == 3:
            num = vetor[1] + vetor[2]
            vetor.append(num)
    matriz.append(vetor)
    vetor = []

for i in range(linhas):
    for j in range(colunas):
        if j == 3:
            num = matriz[i][3]
            vetor.append(num)
        print(f'{matriz[i][j]:^5}', end = ' ')
    print()

print('-'*23)

media_notas = sum(vetor)/linhas
nota_maxima = max(vetor)
indice_max = vetor.index(nota_maxima)
matricula = matriz[indice_max][0]

print(f'A nota máxima foi {nota_maxima}, referente ao aluno {matricula}.')
print(f'A média das notas finais vale {media_notas}.')
