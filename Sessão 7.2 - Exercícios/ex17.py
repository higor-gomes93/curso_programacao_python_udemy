'''
Leia uma matriz 10 x 3 com as notas de 10 alunos em 3 provas. Em seguida, escreva o número de alunos cuja pior
nota foi na prova 1, o número de alunos cuja pior nota foi na prova 2, e o número de alunos cuja pior nota foi
na prova 3. Em caso de empate das piores notas de um aluno, o critério de desempate é arbitrário, mas o aluno
deve ser contabilizado apenas uma vez.
'''

import random as r 

matriz = []
vetor = []
alunos = 10
provas = 3
notas = range(0, 11)
cont_1 = 0
cont_2 = 0
cont_3 = 0

for i in range(alunos):
    for j in range(provas):
        nota = r.choice(notas)
        vetor.append(nota)
    if min(vetor) == vetor[0]:
        cont_1 += 1
    elif min(vetor) == vetor[1]:
        cont_2 += 1
    elif min(vetor) == vetor[2]:
        cont_3 += 1
    matriz.append(vetor)
    vetor = []

for i in range(alunos):
    for j in range(provas):
        print(f'{matriz[i][j]:^5}', end = ' ')
    print()

print('-'*16)

print(f'{cont_1} alunos tiveream a menor nota na prova 1.')
print(f'{cont_2} alunos tiveream a menor nota na prova 2.')
print(f'{cont_3} alunos tiveream a menor nota na prova 3.')
