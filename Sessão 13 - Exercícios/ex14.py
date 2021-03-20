'''
Dado um arquivo contendo um conjunto de nome e data de nascimento (DD MM AAAA,
isto é, 3 inteiros em sequência), faça um programa que leia o nome do arquivo e
a data de hoje e construa outro arquivo contendo o nome e a idade de cada pessoa
do primeiro arquivo.
'''

raiz = 'c:/Users/Higor H/Documents/Estudos/Python'
pasta1 = raiz + '/Curso de Programação em Python (Udemy)/Sessão 13 - Exercícios/ex14_1.txt'
pasta2 = raiz + '/Curso de Programação em Python (Udemy)/Sessão 13 - Exercícios/ex14_2.txt'
data_hoje = '18/04/2020'

with open(pasta1, 'w', encoding='UTF-8') as arquivo1:
    while True:
        comando = input('Deseja adicionar? ')
        if comando.lower() == "sim":
            nome = input('Digite o nome: ')
            data = input('Digite a data de nascimento: ')
            arquivo1.write(f'{nome} - {data}\n')
        else:
            print('Até logo!')
            break

with open(pasta1, 'r', encoding='UTF-8') as arquivo2:
    dados = arquivo2.readlines()

with open(pasta2, 'w', encoding='UTF-8') as arquivo3:
    for i in dados:
        data_nascimento = i.split()[-1]
        nome = i.split()[0]
        if int(data_hoje.split('/')[2]) > int(data_nascimento.split('/')[2]):
            anos = int(data_hoje.split('/')[2]) - int(data_nascimento.split('/')[2])
        else:
            print('Nascimento futuro.')
        if int(data_hoje.split('/')[1]) < int(data_nascimento.split('/')[1]):
            idade = anos - 1
        else:
            idade = anos
        arquivo3.write(f'{nome} - {idade} anos.\n')
