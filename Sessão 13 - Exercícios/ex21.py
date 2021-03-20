'''
Crie um programa que receba como entrada o número de alunos de uma disciplina. Aloque dinamicamente
dois vetores para armazenar as informações a respeito desses alunos. O primeiro vetor contém o nome
dos alunos e o segundo contém suas notas finais. Crie um arquivo que armazene, a cada linha, o nome
do aluno e sua nota final. No fim, mostre o nome do aluno com a maior nota.
'''

from random import choice, uniform

raiz = 'c:/Users/Higor H/Documents/Estudos/Python'
pasta = raiz + '/Curso de Programação em Python (Udemy)/Sessão 13 - Exercícios/ex21.txt'

nomes = ['Miguel', 'Arthur', 'Heitor', 'Bernardo', 'Théo', 'Davi', 'Gabriel', 'Pedro', 'Samuel'
, 'Lorenzo', 'Benjamin', 'Matheus', 'Lucas', 'Benício', 'Gael', 'Joaquim', 'Nicolas', 'Henrique'
, 'Rafael', 'Isaac', 'Guilherme', 'Murilo', 'Lucca', 'Gustavo', 'João Miguel', 'Noah', 'Felipe'
, 'Anthony', 'Enzo', 'João Pedro', 'Pietro', 'Bryan', 'Daniel', 'Pedro Henrique', 'Enzo Gabriel'
, 'Leonardo', 'Vicente', 'Valentim', 'Eduardo', 'Antônio', 'Emanuel', 'Davi Lucca', 'Bento', 'João'
, 'João Lucas', 'Caleb', 'Levi', 'Vitor', 'Enrico', 'Cauã', 'Caio', 'Vinícius', 'Henry', 'João Gabriel'
, 'Augusto', 'Ravi', 'Francisco', 'Otávio', 'Davi Lucas', 'João Guilherme', 'Thomas', 'Ícaro'
, 'Theodoro', 'João Vitor', 'Luiz Miguel', 'Yan', 'Yuri Thiago', 'Arthur Miguel', 'Nathan', 'Erick'
, 'Breno', 'Luiz Felipe', 'Anthony Gabriel', 'Martin', 'Matteo', 'Oliver', 'Arthur Gabriel', 'Ryan'
, 'Raul', 'Luan', 'Tomás', 'Mathias', 'Davi Luiz', 'Pedro Lucas', 'Derick', 'Vitor Hugo', 'Kauê'
, 'Lucas Gabriel', 'Arthur Henrique', 'Rodrigo', 'Bruno', 'Davi Miguel', 'Yago', 'José', 'Pedro Miguel'
, 'Luiz Henrique', 'Hugo', 'Otto', 'Josué']
sobrenomes = ['Silva', 'Souza', 'Costa', 'Santos', 'Oliveira', 'Pereira', 'Rodrigues', 'Almeida'
, 'Nascimento', 'Lima', 'Araújo', 'Fernandes', 'Carvalho', 'Gomes', 'Martins', 'Rocha', 'Ribeiro'
, 'Alves', 'Monteiro', 'Mendes', 'Barros', 'Freitas', 'Barbosa', 'Pinto', 'Moura', 'Cavalcanti'
, 'Dias', 'Castro', 'Campos', 'Cardoso']

total_de_alunos = int(input('Quantos alunos estão nessa disciplina? '))

with open(pasta, 'w', encoding='UTF-8') as arquivo:
    for i in range(total_de_alunos):
        aluno = choice(nomes) + ' ' + choice(sobrenomes)
        nota = round(uniform(0, 10.1),2)
        arquivo.write(f'Nome: {aluno} - Nota: {nota}\n')

with open(pasta, 'r', encoding='UTF-8') as arquivo:
    dados = arquivo.read().split('\n')
    dados.pop()

notas = [float(i.split()[-1]) for i in dados]
aluno_top = ''

for i in dados:
    if float(i.split()[-1]) == max(notas):
        for j in range(1,len(i.split())):
            if i.split()[j] != '-':
                aluno_top += f'{i.split()[j]} '
            else:
                break

print(f'Aluno com a melhor nota - {aluno_top.strip()}')
