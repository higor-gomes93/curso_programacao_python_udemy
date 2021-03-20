'''
Faça um programa que leia um arquivo que contenha as dimensões de uma matriz (linha e 
coluna), a quantidade de posições que serão anuladas, e as posições a serem anuladas 
(linha e coluna). O programa lê esse arquivo e, em seguida, produz um novo arquivo
com a matriz com as dimensões dadas no arquivo lido, e todas as posições especificadas
no arquivo ZERADAS e o restante recebendo valor 1.
'''

raiz = 'c:/Users/Higor H/Documents/Estudos/Python'
pasta1 = raiz + '/Curso de Programação em Python (Udemy)/Sessão 13 - Exercícios/ex17_1.txt'
pasta2 = raiz + '/Curso de Programação em Python (Udemy)/Sessão 13 - Exercícios/ex17_2.txt'

with open(pasta1, 'w', encoding='UTF-8') as arquivo:
    linhas = int(input('Informe o número de linhas: '))
    colunas = int(input('Informe o número de colunas: '))
    while True:
        anuladas = input('Informe quantas posições serão anuladas: ')
        if int(anuladas) <= linhas*colunas:
            arquivo.write(f'{linhas} {colunas} {anuladas}\n')
            break
        else:
            print('Número inválido, superior ao total de elementos da matriz.')
    for i in range(int(anuladas)):
        while True:
            posicao = input(f'Digite a posição da {i+1}ª anulação: ')
            if int(posicao.split()[0]) < linhas and int(posicao.split()[1]) < colunas:
                arquivo.write(f'{posicao}\n')
                break
            else:
                print('Posição inválida, fora dos intervalos.')

with open(pasta1, 'r', encoding='UTF-8') as arquivo:
    texto = arquivo.read().split('\n')
    texto.pop()
    linhas = int(texto[0].split()[0])
    colunas = int(texto[0].split()[1])
    anuladas = int(texto[0].split()[2])
    posicoes = [(int(i[0]), int(i[2])) for i in texto[1:]]
    matriz = [[1 if (i, j) in posicoes else 0 for j in range(colunas)] for i in range(linhas)]

with open(pasta2, 'w', encoding='UTF-8') as arquivo:
    for i in range(linhas):
        for j in range(colunas):
            arquivo.write(f'{matriz[i][j]} ')
        arquivo.write('\n')
