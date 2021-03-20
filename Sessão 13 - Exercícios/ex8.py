'''
Faça um programa que leia o conteúdo de um arquivo e crie um arquivo com o mesmo conteúdo, 
mas com todas as letras minúsculas convertidas para maiúsculas. Os nomes dos arquivos
serão fornecidos, via teclado, pelo usuário.
'''

raiz = 'c:/Users/Higor H/Documents/Estudos/Python/Curso de Programação em Python (Udemy)'
pasta_leitura = raiz + '/Notas de Aula/' + input('Digite o nome do arquivo a ser lido: ')
pasta_escrita = raiz + '/Sessão 13 - Exercícios/' + input('Digite o nome do arquivo novo: ')

with open(pasta_leitura, 'r', encoding='UTF-8') as leitura:
    texto = leitura.read()

with open(pasta_escrita + '.txt', 'w', encoding='UTF-8') as arquivo:
    for caracter in texto:
        arquivo.write(caracter.upper())
