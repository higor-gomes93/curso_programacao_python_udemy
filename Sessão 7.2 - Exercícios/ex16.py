'''
Faça um programa para corrigir uma prova com 10 questões de múltipla escolha (a, b, c, d ou e), em uma turma com
3 alunos. Cada questão vale 1 ponto. Leia o gabarito, e para cada aluno leia sua matrícula (número inteiro), e suas
respostas. Calcule e escreva para cada aluno: sua matrícula, suas respostas e sua nota. Escreva também o percentual
de aprovação, assumindo média 7.0.
'''

import random as r 

matriz = []
vetor = []
alunos = 3
questoes = 10
alternativas = ['a', 'b', 'c', 'd', 'e']
gabarito = []
elementos = []
valor = []
chave = []
dicionario = {}
dicio_aux = {'Respostas':'','Acertos':''}
cont = 0
aprov = 0

while len(chave) < alunos:
    ident = r.randrange(145000, 149000)
    chave.append(ident)
    print(f'Identificação do {len(chave)}º aluno: {chave[len(chave)-1]}')

print('-'*19)
print('Gabarito:')
for i in range(questoes):
    questao = r.choice(alternativas)
    gabarito.append(questao)
    print(gabarito[i], end = ' ')
print()

print('-'*19)

print(f'Respostas dos {alunos} alunos:')
for i in range(alunos):
    for j in range(questoes):
        resp = r.choice(alternativas)
        vetor.append(resp)
    matriz.append(vetor)
    vetor = []

for i in range(alunos):
    for j in range(questoes):
        print(matriz[i][j], end = ' ')
    print()

print('-'*19)

for i in range(alunos):
    for j in range(questoes):
        num = matriz[i][j]
        if num == gabarito[j]:
            cont += 1
        vetor.append(num)
    if cont >= 7:
        aprov += 1
    elementos.append(vetor)
    elementos.append(cont)
    dicio_aux[f'Respostas'] = elementos[0]
    dicio_aux[f'Acertos'] = elementos[1]
    valor.append(dicio_aux)
    elementos = []
    vetor = []
    cont = 0
    dicio_aux = {'Respostas':'','Acertos':''}
    dicionario[chave[i]] = valor[i]

for i in dicionario:
    print(f'Aluno {i}: {dicionario[i]}')

print('-'*19)

print(f'Taxa de aprovação: {round(aprov/alunos,3)*100} %.')
